from tkinter import *
from tkinter import ttk, filedialog, messagebox
from ttkthemes import ThemedTk
import base64
import temp_balllot
import random
import os
import client
from PIL import Image,ImageTk
import doc_gen

sc = ThemedTk(theme="arc")
sc.title("Login")
sc.iconbitmap("gov2.ico")
sc.minsize(600, 400)
sc.resizable(False,False)
te1 = StringVar()
te2 = StringVar()

ff1 = Frame(sc, height=100, width=600)
ff1.grid(column=0, row=0, columnspan=10)


##LOGIN##
def fb1():
    global photo
    temp=recv_login_data(te1.get(),te2.get())
    item=eval(str(temp))
    if item==False:

        txt = "(Incorrect username or voter id number.) "
        tl1 = Label(f2, text=txt, bg="#8fb7f7")
        tl1.grid(column=3, row=2)
        def fbr2():
            e1.delete(0, END)
            e2.delete(0, END)
            tl1.destroy()
            b1 = ttk.Button(f2, text="Login", command=fb1)
            b1.grid(column=2, row=9)
            te1.set("")
            te2.set("")

        br = ttk.Button(f2, text="Retry", command=fbr2)
        br.grid(column=2, row=9)

    else:
        sc.destroy()
        if str(item[10])=="None":
            temp_balllot.min(item)
        elif str(item[10])!="None":
            messagebox.showinfo(message="You have already vote.\nFor further information visit related office.")


def ffp():
    messagebox.showinfo(message="Please visit related office.")


f1 = Frame(sc, height=210, width=35)
f2 = LabelFrame(text="Login", height=100, width=460, padx=50, pady=50, background="#8fb7f7")
l1 = ttk.Label(f2, text="Username:", background="#8fb7f7")
l2 = ttk.Label(f2, text="Voter ID Number:", background="#8fb7f7")
# b3 = Button(f2, text="Forget Password?", bd=0, bg="#8fb7f7", command=ffp,fg="#a19f9a")
e1 = ttk.Entry(f2, textvariable=te1)
e2 = ttk.Entry(f2, textvariable=te2, show="*")


##Cancel##
def fb2():
    e1.delete(0, END)
    e2.delete(0, END)

def login():
    try:
        fb1()
    except OSError as msg:
        messagebox.showerror(message=str(msg)+"\n Please try later.")

    # except:
    #     messagebox.showerror(message="Sorry, Something went wrong.\n Please try later.")
    #     exit()


b1 = ttk.Button(f2, text="Login", command=login)
b2 = ttk.Button(f2, text="Cancel", command=fb2)
f1.grid(column=0, rowspan=5, row=1, sticky=NSEW)
f2.grid(column=1, row=1, sticky=NSEW, )
l1.grid(column=1, row=2)
l2.grid(column=1, row=3)
e1.grid(column=2, row=2,sticky=W,pady=5)
e2.grid(column=2, row=3,sticky=W,pady=5)
b1.grid(column=2, row=9,pady=5)
b2.grid(column=3, row=9,pady=5)
# b3.grid(column=1, row=12)


def fb3():
    pass
def recv_login_data(user,pas):
    temp=client.recv(user,pas)
    data=eval(temp)
    return data


def send_to_server(temp):
    print(temp)
    result=client.send(temp)
    return result

sc.mainloop()