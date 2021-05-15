from tkinter import *
from tkinter import ttk, filedialog, messagebox
from ttkthemes import ThemedTk
import base64
import ballot_page
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
te3 = StringVar()
te4 = StringVar()
te5 = StringVar()
te6 = StringVar()
te10 = StringVar()
tctzn = StringVar()
tcon = StringVar()
tgen = StringVar()
phdir = StringVar()
date = StringVar()
te11 = StringVar()
te12 = StringVar()
selfil = StringVar()
us = StringVar()
up = StringVar()

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
            ballot_page.min(item)
        elif str(item[10])!="None":
            messagebox.showinfo(message="You have already vote.\nFor further information visit related office.")
            exit()

def ffp():
    messagebox.showinfo(message="Please visit related office.")


f1 = Frame(sc, height=210, width=35)
f2 = LabelFrame(text="Login", height=100, width=460, padx=50, pady=50, background="#8fb7f7")
l1 = ttk.Label(f2, text="Username:", background="#8fb7f7")
l2 = ttk.Label(f2, text="Voter ID Number:", background="#8fb7f7")
# b3 = Button(f2, text="Forget Password?", bd=0, bg="#8fb7f7", command=ffp,fg="#a19f9a")
e1 = ttk.Entry(f2, textvariable=te1)
e2 = ttk.Entry(f2, textvariable=te2, show="*")


##SINGUP##
def fb2():
    f2.destroy()
    f3 = LabelFrame(sc, text="SingUp", height=100, width=200, padx=50, pady=50, background="#8fb7f7")
    l3 = ttk.Label(f3, text="Full Name:", background="#8fb7f7")
    l4 = ttk.Label(f3, text="Email:", background="#8fb7f7")
    l5 = ttk.Label(f3, text="Phone Number:", background="#8fb7f7")
    l7 = ttk.Label(f3, text="Gender:", background="#8fb7f7")
    l8 = ttk.Label(f3, text="DOB:", background="#8fb7f7")
    l9 = ttk.Label(f3, text="Photo:", background="#8fb7f7")
    l10 = ttk.Label(f3, text="Address:", background="#8fb7f7")
    l11 = ttk.Label(f3, text="Citizenship ID Number:", background="#8fb7f7")

    def fselb():
        global selfil
        global photo
        try:
            selfil = filedialog.askopenfile(title="Select photo", filetypes=(
                ("JPG files", "*.jpg"), ("PNG files", "*.png"),("All files", "*.*")))
            s1 = str(selfil).split("=")
            s2 = s1[1].split(" ")
            selfil = s2[0][1:len(s2[0]) - 1]
            # img=Image.open(selfil)
            # ll=ttk.Label(f3,image=img)
            # ll.grid(column=19,row=19,sticky=E)
            with open(selfil, "rb") as fptr:
                photo = base64.b64encode(fptr.read())
            pho = ttk.Label(f3, text=selfil, background="#8fb7f7")
            pho.grid(column=3, row=8, sticky=E, columnspan=4)
            selb.destroy()
        except FileNotFoundError as msg:
            messagebox.showerror(message=str(msg)+"\nCheck file format.")

    def fcap():
        global photo
        pass

    def fcont():
        msg=messagebox.askyesno(message="Are you sure want continue.\nYou will be unable to revisit this page.")
        if msg==True:
            f3.destroy()
            f4 = LabelFrame(sc, text="Create Password", height=100, width=200, padx=50, pady=50, background="#8fb7f7")
            l11 = ttk.Label(f4, text="Enter Password:", background="#8fb7f7")
            l12 = ttk.Label(f4, text="Re-Enter Password:", background="#8fb7f7")
            e11 = ttk.Entry(f4, textvariable=te11, show="*")
            e12 = ttk.Entry(f4, textvariable=te12, show="*")

        else:
            pass

        def fsin():
            global photo,selfil

            if str(te11.get())!=str(te12.get()):
                messagebox.showerror(message="Incorrect combination.\nPlease retype your password.")
                te11.set("")
                te12.set("")
            else:
                try:
                    # print(te3.get(),"\t",te4.get(),"\t",te5.get(),"\n",tcon.get(),"\t",date.get(),"\t",tgen.get(),"\t",phdir.get(),"\t",te11.get(),"\t",te12.get(),"\t",selfil)
                    vid=random.randint(1000,100000000)
                    temp = (te3.get(), te4.get(), te5.get(), tcon.get(), tgen.get(), date.get(), te11.get(), photo,tctzn.get(),vid,None)
                    result=send_to_server(temp) #create connection and send to server
                    print(result)
                except NameError:
                    messagebox.showerror(message="Make sure all the filed is filled.")
                    pass


                def doc(result):
                    if result=="yes":

                        try:
                            t1=filedialog.askdirectory(title="Choose location to save confirmation page.")
                            doc_gen.pdf(temp, t1,selfil)
                            messagebox.showinfo(message="User added sucessfully!")
                            sc.destroy()
                        except NotADirectoryError as msg:
                            messagebox.showerror(message=str(msg)+str("Try another locatiom"))
                            doc(result)
                        except IsADirectoryError as mms:
                            messagebox.showerror(message=str(mms)+str("Try another locatiom"))
                            doc(result)
                        except FileNotFoundError as m1:
                            messagebox.showerror(message=str(m1)+str("Try another locatiom"))
                            doc(result)
                        except PermissionError as m2:
                            messagebox.showerror(message=str(m2)+str("Try another locatiom"))
                            doc(result)

                    elif result=="not":
                        messagebox.showinfo(message="User already exist!\n Please visit related office for further information.")
                        sc.destroy()

                doc(result)

        b5 = ttk.Button(f4, text="SingUp", command=fsin)

        def fbb2():
            f4.destroy()
            fb2()

        b6 = ttk.Button(f4, text="Back", command=fbb2)

        f4.grid(column=3, row=3)
        l11.grid(column=3, row=2, sticky=E)
        l12.grid(column=3, row=3, sticky=E)
        e11.grid(column=4, row=2, sticky=W,pady=1)
        e12.grid(column=4, row=3, sticky=W,pady=1)
        b6.grid(column=3, row=13, sticky=W)
        b5.grid(column=5, row=13, sticky=E)

    nb = ttk.Button(f3, text="Continue", command=fcont)

    def fbb1():
        f3.destroy()
        fb1()

    cb = ttk.Button(f3, text="Back", command=fbb1)
    e3 = ttk.Entry(f3, textvariable=te3)
    e4 = ttk.Entry(f3, textvariable=te4)
    e5 = ttk.Entry(f3, textvariable=te5, width=14)
    e10=ttk.Entry(f3,textvariable=tcon)
    ectzn = ttk.Entry(f3, textvariable=tctzn)

    e8 = ttk.Entry(f3, textvariable=date)
    e8.insert(0, "YYYY/MM/DD")

    def dclr(event):
        e8.delete(0, END)

    e8.bind("<Button-1>", dclr)
    gen1 = ttk.Radiobutton(f3, variable=tgen, value="M", text="Male")
    gen2 = ttk.Radiobutton(f3, variable=tgen, value="F", text="female")

    selb = ttk.Button(f3, text="Browse", command=fselb)
    cap=ttk.Button(f3,text="Capture",command=fcap)
    f3.grid(column=1, row=0,pady=50,sticky=NS)
    l3.grid(column=2, row=2, sticky=E)
    e3.grid(column=3, row=2, sticky=W,pady=2)
    l4.grid(column=2, row=4, sticky=E)
    e4.grid(column=3, row=4, sticky=W,pady=2)
    e5.grid(column=3, row=5,sticky=W,pady=2)
    l5.grid(column=2, row=5, sticky=E)
    gen1.grid(column=3, row=6, sticky=W)
    gen2.grid(column=4, row=6, sticky=E)

    l7.grid(column=2, row=6, sticky=E)
    l8.grid(column=2, row=7, sticky=E)
    e8.grid(column=3, row=7, sticky=E,pady=2)
    l9.grid(column=2, row=8, sticky=E)
    l10.grid(column=2, row=3, sticky=E)
    e10.grid(column=3,row=3,sticky=W,pady=2)
    l11.grid(column=2, row=9, sticky=E)
    ectzn.grid(column=3, row=9, sticky=W,pady=2)
    selb.grid(column=3, row=8, sticky=W,pady=2)
    cap.grid(column=4, row=8, sticky=E, pady=2,padx=2)
    nb.grid(column=3, row=10, sticky=SE,pady=10)
    cb.grid(column=1, row=10, sticky=SW,pady=10)


def login():
    try:
        fb1()
    except OSError as msg:
        messagebox.showerror(message=str(msg)+"\n Please try later.")
        exit()
    # except:
    #     messagebox.showerror(message="Sorry, Something went wrong.\n Please try later.")
    #     exit()


b1 = ttk.Button(f2, text="Login", command=login)
b2 = ttk.Button(f2, text="Sing Up", command=fb2)
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