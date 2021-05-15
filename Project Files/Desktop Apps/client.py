import socket
import time
global result
from tkinter import messagebox

def ipfile():
    try:
        with open("ip.txt","r") as ip:
            add=ip.readline()
            return add
    except:
        messagebox.showinfo(message="please configure ip address in file named ip.txt")
        return "192.168.100.32"


def send(temp):


    s = socket.socket()

    host = ipfile()

    port = 9999


    global timing
    timing=0
    try:
        s.connect((host, port))
        print("Connected")
    except:
        print("Connection can not be created.")



    def sending(temp):
        global timing
        while True:
            try:
                temp1=str("su, "+str(temp))
                print(temp1)
                s.send(str.encode(temp1))
                print("Sent")
                temp = s.recv(1024)
                result = temp.decode("utf-8")
                return result
                break


            except OSError as msg:

                messagebox.showerror(message=str(msg) + "\n Please try later.")

                exit()

            except:

                messagebox.showerror(message="Sorry, Something went wrong.\n Please try later.")

                exit()
    return sending(temp)



def recv(user,pas):

    s = socket.socket()

    host = ipfile()

    port = 9999


    global timing,result
    timing=0
    try:
        s.connect((host, port))
        print("Connected")
    except:
        print("Connection can not be created.")





    def sending(user,pas):
        global timing,result
        while True:

                temp=str("lg, "+user+"//a/"+pas)
                s.send(str.encode(temp))
                print("Sent")
                temp = s.recv(9000000)
                result=temp.decode("utf-8")
                break
        s.close()


    sending(user, pas)
    return result


def sendvote(party,item):

    s = socket.socket()

    host = ipfile()

    port = 9999

    global timing, result
    timing = 0
    try:
        s.connect((host, port))
        print("Connected")
    except:
        print("Connection can not be created.")

    def sending(party):
        global timing
        while True:
            temp = str("vt, " + "//a/" + str(party)+str("vid")+str(item[9]))
            s.send(str.encode(temp))
            messagebox.showinfo(message="Your candidate has been sent.")
            break
        s.close()
    sending(party)
