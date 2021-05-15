import socket
import server_side_db
import sys

import _thread as thr

import time

from queue import Queue

global timing,conn,address

NUMBER_OF_THREADS = 2

JOB_NUMBER = [1, 2]

queue = Queue()

def main():

    # Create a Socket ( connect two computers)

    def create_socket():
        try:

            global host

            global port

            global s

            host = ""

            port = 9999

            s = socket.socket()


        except socket.error as msg:

            print("Socket creation error: " + str(msg))


    # Binding the socket and listening for connections

    def bind_socket():
        global host

        global port

        global s
        global conn,address

        host = ""
        port = 9999


        s.bind((host, port))
        print("Binding the Port: " + str(port))
        s.listen(5)





    def resend(conn,result):  #resend data

            global timing
            timing = 0

            # try:
            #
            #     print("Connected")
            # except:
            #     print("Connection can not be created.")

            temp1 = str(result)
            conn.send(str.encode(temp1))
            #print("Sent")




    def recv_data(conn):
        global address
        while 1:
            # print("Connection has been established :" + address[0])
            s.setblocking(1)  # prevents timeout
            req = str(conn.recv(9000000), "utf-8")  ###knowing type of request
            com = req[:4]
            data = req[4:]
            if com == "su, ":

                signup(conn,data)

            elif com == "lg, ":

                login(conn, data)

            elif com == "vt, ":

                print("Vote")
                data=data[4:]
                print(data)
                server_side_db.vote(data)

        conn.close()


    def tread():
        global conn,address
        while 1:
            conn, address = s.accept()
            thr.start_new(recv_data,(conn,))




    # def fun1():
    #     while True:
    #         create_socket()
    #         bind_socket()
    #         recv_data()

    def signup(conn,data):

        li = eval(data)  ##Converting to original data type from string type
        #print(type(li))
        #print(li[7])
        result=server_side_db.write(li)
        resend(conn,result)

    def login(conn,data):
        global timing
        global host,port
        timing=0
        #print("inside login")
        user,pas=data.split("//a/")
        result=server_side_db.read(user, pas)
        resend(conn,result)

    # def start():
    #     for i in range(2):
    #         t1=threading.Thread(target=fun1)
    #         t1.daemon=True
    #         t1.start()
    #
    # start()
    create_socket()
    bind_socket()
    tread()