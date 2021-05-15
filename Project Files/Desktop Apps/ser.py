# import socket
# global port
# global host
# host=""
# port=9999
#
# s=socket.socket()
# s.bind((host,port))
# s.listen(5)
# while True:
#     conn,add=s.accept()
#     while True:
#         data=conn.recv(9000000)
#         b=str.encode("Hi")
#         conn.send(b)
#         print(data)
#     conn.close()


import socket
import server_side_db
import sys

import threading

import time

from queue import Queue

global timing

NUMBER_OF_THREADS = 2

JOB_NUMBER = [1, 2]

queue = Queue()





# Create a Socket ( connect two computers)

def create_socket():
    while 1:
        try:

            global host

            global port

            global s

            host = ""

            port = 9999

            s = socket.socket()
            print("sc")
            break



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
        print("Sent")



def recv_data():
    while 1:
        conn, address = s.accept()
        print("Connection has been established :" + address[0])
        s.setblocking(1)  # prevents timeout
        req = str(conn.recv(9000000), "utf-8")  ###knowing type of request
        com = req[:4]
        data = req[4:]
        if com == "su, ":

            signup(data)


        elif com == "lg, ":

            login(conn, data)

        elif com == "vt, ":
            print("Vote")
            data=data[4:]
            server_side_db.vote(data)

        break
    conn.close()




def fun1():
    create_socket()
    bind_socket()
    recv_data()

def signup(data):

    li = eval(data)  ##Converting to original data type from string type
    print(type(li))
    print(li[7])
    server_side_db.write(li)

def login(conn,data):
    global timing
    global host,port
    timing=0
    print("inside login")
    user,pas=data.split("//a/")
    result=server_side_db.read(user, pas)
    resend(conn,result)




fun1()
