########login##########
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import sqlite3
import base64
import ballot_page
import os
import client
from PIL import Image,ImageTk
import doc_gen

sc = Tk()
sc.title("Login")
sc.iconbitmap("ic.ico")
sc.minsize(800, 600)
sc.maxsize(800, 600)
te1 = StringVar()
te2 = StringVar()
te3 = StringVar()
te4 = StringVar()
te5 = StringVar()
te6 = StringVar()
tcon = StringVar()
tgen = StringVar()
phdir = StringVar()
date = StringVar()
te11 = StringVar()
te12 = StringVar()
selfil = StringVar()
us = StringVar()
up = StringVar()

country = ["Nepal", "India", "China"]

c = sqlite3.connect("info.db")
c.execute(
    '''CREATE TABLE IF NOT EXISTS info(usr text, eml text, phon text, cou text, gen char ,dob text, pw text,ph BlOB)''')

ff1 = Frame(sc, height=130, width=500)
ff1.grid(column=0, row=0, columnspan=10)


##ForgetPass#
def ffp():
    f2.destroy()
    fl = LabelFrame(sc, text="Change Password", padx=50, pady=50, bg="light green", height=100, width=200)
    e1 = Label(fl, text="Username:", bg="light green")
    e2 = Label(fl, text="Phone Number:", bg="light green")
    ee1 = Entry(fl, textvariable=us)
    ee3 = Label(fl, text="(Including country code)", bg="light green")
    ee2 = Entry(fl, textvariable=up)

    def fb():
        op = StringVar()
        np = StringVar()
        tc = c.execute("SELECT usr,pw,phon from info")
        for item in tc:
            if item[0] == us.get():
                if item[2] == up.get():
                    fl.destroy()
                    ff2 = LabelFrame(sc, text="Change Password", padx=50, pady=50, bg="light green", height=100,
                                     width=200)
                    e1 = Label(ff2, text="Enter new password:", bg="light green")
                    e2 = Label(ff2, text="Renter new password:", bg="light green")
                    ee1 = Entry(ff2, textvariable=op, show="*")
                    ee2 = Entry(ff2, textvariable=np, show="*")

                    def chn():
                        if op.get() == np.get():
                            c.execute("""UPDATE info set pw = ? where usr= ? """, (np.get(), item[0]))
                            c.commit()
                            messagebox.showinfo(message="Changed!")

                    bb1 = Button(ff2, text="Change", command=chn)
                    bb1.grid(column=2, row=3, sticky=NSEW)
                    ee1.grid(column=2, row=1, sticky=W)
                    ee2.grid(column=2, row=2, sticky=W)
                    e1.grid(column=1, row=1, sticky=E)
                    e2.grid(column=1, row=2, sticky=E)
                    ff2.grid(column=2, row=1, sticky=NSEW)

    bb = Button(fl, text="Find", command=fb)
    bb.grid(column=2, row=3)

    e1.grid(column=1, row=1, sticky=E)
    e2.grid(column=1, row=2, sticky=E)
    ee1.grid(column=2, row=1, sticky=W)
    ee2.grid(column=2, row=2, sticky=W)
    ee3.grid(column=3, row=2, sticky=W)
    fl.grid(column=2, row=1, sticky=NSEW)


##LOGIN##
def fb1():
    global photo
    temp=recv_login_data(te1.get(),te2.get())
    item=eval(str(temp))
    if item==False:

        txt = "Incorrect username or password. "
        tl1 = Label(f2, text=txt, bg="light green")
        tl1.grid(column=3, row=2)
        def fbr2():
            e1.delete(0, END)
            e2.delete(0, END)
            tl1.destroy()
            b1 = Button(f2, text="Login", command=fb1)
            b1.grid(column=2, row=9)

        br = Button(f2, text="Retry", command=fbr2)
        br.grid(column=2, row=9)

    else:
        sc.destroy()

        ballot_page.min(item)

        # if item[0] == te1.get():
        #     if item[1] == te2.get():
        #         f2.destroy()
        #         f5 = LabelFrame(sc, text=item[0], height=100, width=200, padx=50, pady=50, background="light green")
        #         l13 = Label(f5, text="Full Name: " + item[0], background="light green")
        #         l14 = Label(f5, text="Email: " + item[2], background="light green")
        #         l15 = Label(f5, text="Phone Number: " + item[3], background="light green")
        #         l16 = Label(f5, text="Country: " + item[4], background="light green")
        #         l17 = Label(f5, text="Gender: " + item[5], background="light green")
        #         l18 = Label(f5, text="DOB: " + item[6], background="light green")
        #         with open("np.png", "wb") as fptr:
        #             fptr.write(base64.b64decode(item[7]))
        #         img1 = PhotoImage("np.png")
        #         l19 = Label(f5, image=img1)
        #         os.remove("np.png")
        #
        #         f5.grid(column=3, row=3)
        #         l13.grid(column=2, row=2, sticky=W)
        #         l14.grid(column=2, row=3, sticky=W)
        #         l15.grid(column=2, row=4, sticky=W)
        #         l16.grid(column=2, row=5, sticky=W)
        #         l17.grid(column=2, row=6, sticky=W)
        #         l18.grid(column=2, row=7, sticky=W)
        #         l19.grid(column=3, row=1, sticky=E)
        #
        #     else:
        #         tl2 = Label(f2, text="Wrong Password!!!", bg="light green")
        #         tl2.grid(column=3, row=3)
        #         b1.destroy()
        #
        #
        #
        # else:
        #     global txt
        #
        #     b1.destroy()
        #
        #     def fbr1():
        #         e1.delete(0, END)
        #         e2.delete(0, END)
        #         tl1.destroy()
        #         b1 = Button(f2, text="Login", command=fb1)
        #         b1.grid(column=2, row=9)
        #
        #     br = Button(f2, text="Retry", command=fbr1)
        #     br.grid(column=2, row=9)


f1 = Frame(sc, height=210, width=50)
f2 = LabelFrame(text="Login", height=100, width=460, padx=50, pady=50, background="light green")
l1 = Label(f2, text="Username:", background="light green")
l2 = Label(f2, text="Passwords:", background="light green")
b3 = Button(f2, text="Forget Password?", bd=0, bg="light green", command=ffp)
e1 = Entry(f2, textvariable=te1)
e2 = Entry(f2, textvariable=te2, show="*")


##SINGUP##
def fb2():
    f2.destroy()
    f3 = LabelFrame(sc, text="SingUp", height=100, width=200, padx=50, pady=50, background="light green")
    l3 = Label(f3, text="Full Name:", background="light green")
    l4 = Label(f3, text="Email:", background="light green")
    l5 = Label(f3, text="Phone Number:", background="light green")
    l6 = Label(f3, text="Country:", background="light green")
    l7 = Label(f3, text="Gender:", background="light green")
    l8 = Label(f3, text="DOB:", background="light green")
    l9 = Label(f3, text="Photo:", background="light green")

    def fselb():
        global selfil
        global photo
        selfil = filedialog.askopenfile(title="Select photo", filetypes=(
            ("JPG files", "*.jpg"), ("PNG files", "*.png"),("All files", "*.*")))
        s1 = str(selfil).split("=")
        s2 = s1[1].split(" ")
        selfil = s2[0][1:len(s2[0]) - 1]
        # img=Image.open(selfil)
        # ll=Label(f3,image=img)
        # ll.grid(column=19,row=19,sticky=E)
        with open(selfil, "rb") as fptr:
            photo = base64.b64encode(fptr.read())
        pho = Label(f3, text=selfil, background="light green")
        pho.grid(column=3, row=8, sticky=E, columnspan=4)
        print(photo)
        selb.destroy()

    def fcont():
        f3.destroy()
        f4 = LabelFrame(sc, text="Create Password", height=100, width=200, padx=50, pady=50, background="light green")
        l11 = Label(f4, text="Enter Password:", background="light green")
        l12 = Label(f4, text="Re-Enter Password:", background="light green")
        e11 = Entry(f4, textvariable=te11, show="*")
        e12 = Entry(f4, textvariable=te12, show="*")

        def fsin():
            global photo,selfil
            te5.set(te6.get() + te5.get())
            # print(te3.get(),"\t",te4.get(),"\t",te5.get(),"\n",tcon.get(),"\t",date.get(),"\t",tgen.get(),"\t",phdir.get(),"\t",te11.get(),"\t",te12.get(),"\t",selfil)
            temp = (te3.get(), te4.get(), te5.get(), tcon.get(), tgen.get(), date.get(), te11.get(), photo)
            send_to_server(temp) #create connection and send to server
            c.execute("INSERT INTO info VALUES (?,?,?,?,?,?,?,?)", temp)
            c.commit()
            messagebox.showinfo(message="User added sucessfully!")
            doc_gen.pdf(temp,selfil)

        b5 = Button(f4, text="SingUp", command=fsin)

        def fbb2():
            f4.destroy()
            fb2()

        b6 = Button(f4, text="Back", command=fbb2)

        f4.grid(column=3, row=3)
        l11.grid(column=3, row=2, sticky=E)
        l12.grid(column=3, row=3, sticky=E)
        e11.grid(column=4, row=2, sticky=W)
        e12.grid(column=4, row=3, sticky=W)
        b6.grid(column=3, row=4, sticky=W)
        b5.grid(column=5, row=4, sticky=E)

    nb = Button(f3, text="Continue", command=fcont)

    def fbb1():
        f3.destroy()
        fb1()

    cb = Button(f3, text="Back", command=fbb1)
    e3 = Entry(f3, textvariable=te3)
    e4 = Entry(f3, textvariable=te4)
    e5 = Entry(f3, textvariable=te5, width=10)


    con = ttk.Combobox(f3, textvariable=tcon, values=country, width=17, justify="left", state="readonly")
    con.set(country[0])

    e55 = Entry(f3, textvariable=te6, width=4)
    e8 = Entry(f3, textvariable=date)
    e8.insert(0, "YYYY/MM/DD")

    def dclr(event):
        e8.delete(0, END)

    e8.bind("<Button-1>", dclr)
    gen1 = ttk.Radiobutton(f3, variable=tgen, value="M", text="Male")
    gen2 = ttk.Radiobutton(f3, variable=tgen, value="F", text="female")

    selb = Button(f3, text="Browse", command=fselb)
    f3.grid(column=1, row=1, sticky=NSEW)
    l3.grid(column=2, row=2, sticky=E)
    e3.grid(column=3, row=2, sticky=W)
    l4.grid(column=2, row=3, sticky=E)
    e4.grid(column=3, row=3, sticky=W)
    l6.grid(column=2, row=4, sticky=E)
    con.grid(column=3, row=4, sticky=W)
    e55.grid(column=3, row=5, sticky=W)
    e5.grid(column=3, row=5, columnspan=2,sticky=E)
    l5.grid(column=2, row=5, sticky=E)
    gen1.grid(column=3, row=6, sticky=W)
    gen2.grid(column=4, row=6, sticky=E)

    l7.grid(column=2, row=6, sticky=E)
    l8.grid(column=2, row=7, sticky=E)
    e8.grid(column=3, row=7, sticky=E)
    l9.grid(column=2, row=8, sticky=E)
    selb.grid(column=3, row=8, sticky=W)
    nb.grid(column=3, row=10, sticky=SE)
    cb.grid(column=1, row=10, sticky=SW)


b1 = Button(f2, text="Login", command=fb1)
b2 = Button(f2, text="Sing Up", command=fb2)
f1.grid(column=0, rowspan=5, row=1, sticky=NSEW)
f2.grid(column=1, row=1, sticky=NSEW, )
l1.grid(column=1, row=2)
l2.grid(column=1, row=3)
e1.grid(column=2, row=2)
e2.grid(column=2, row=3)
b1.grid(column=2, row=9)
b2.grid(column=3, row=9)
b3.grid(column=1, row=12)


def fb3():
    pass
def recv_login_data(user,pas):
    temp=client.recv(user,pas)
    data=eval(temp)
    return data


def send_to_server(temp):
    print(temp)
    client.send(temp)

sc.mainloop()



##########docgen$###########
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import portrait
from reportlab.platypus import Image
from reportlab.lib import colors
from reportlab.graphics import shapes,renderPDF
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code93


def pdf(data,selfil):

    filename=str(data[0])+"_election_.pdf"
    c=canvas.Canvas(filename,pagesize=portrait(A4))
    c.drawInlineImage("gov1.png",20,740,width=None,height=None)
    c.drawInlineImage("gov2.png", 460, 740, width=None, height=None)
    #c.setFont(psfontname="Arial",size=40,leading=0)
    c.drawString(250, 675, "Confidential ! ")
    c.rect(20,430,545,230)
    c.drawString(35,640,"Voter ID: 1")
    c.drawString(35, 625, "Citizenship ID Number: 2")
    usr="Username: "+data[0]
    c.drawString(35, 610,usr)
    pw="Password: "+str(data[6])
    c.drawString(35, 595, pw)
    dob="Date of Birth: "+str(data[5])
    c.drawString(35, 580, dob)
    eml="Email: "+str(data[1])
    c.drawString(35, 565, eml)
    phon="Phone Number: "+str(data[2])
    c.drawString(35, 550, phon)
    add="Address: "+str(data[3])
    c.drawString(35, 535, add)
    c.drawString(35, 520, "Province: 1")
    c.drawInlineImage(selfil, 440, 540, width=115, height=110)
    bar=code93.Extended93(str(data[2]))
    # bar.barHeight=50
    # bar.barWidth=100
    bar.drawOn(c,440,500)





    c.save()
#################bar############
from tkinter import *
import threading
import time
import tkfontchooser
sc=Tk()
sc.minsize(300,300)
sc.resizable(False,False)
sc.title("server_status")
sc.iconbitmap("gov2.ico")
l=Label(sc,font={"10"},fg="green")
i=0
def th():
    i=0
    while 1:
        l2 = Label(sc,font={"10"},fg="green")
        l2["text"]=""
        l2.place(relx=0.5,rely=0.5)
        l["text"]="Server is running."
        l.place(relx=0.30,rely=0.41)
        l2["text"]=">"
        l2.place(relx=0.5,rely=0.5)
        time.sleep(0.5)
        l2["text"] = ">>"
        l2.place(relx=0.5,rely=0.5)
        time.sleep(0.5)
        i+=1
        l2["text"] = ">>>"
        time.sleep(0.5)
        print(i)
        l2.place(relx=0.5,rely=0.5)
        l2.destroy()

t=threading.Thread(target=th)
t.daemon=True
t.start()

sc.mainloop()



####Bllot###########
from tkinter import *
import os
import base64
from PIL import ImageTk,Image
from tkinter import messagebox
import client

def min(item):
    global party
    sc = Tk()
    sc.title("ballot_page")
    sc.minsize(1500, 700)
    sc.iconbitmap("ic.ico")

    f1 = Frame(sc, bg="blue", height=123, width=2000)
    c = Canvas(f1, width=120, height=100)

    pd = item[7]
    with open("np.png", "wb") as fptr:
                fptr.write(base64.b64decode(item[7]))
    i = Image.open("np.png")
    i.thumbnail((120, 105))
    i.save("n.png")
    m = Image.open("n.png")
    k = ImageTk.PhotoImage(m)
    # c.create_image(image=k)



    gov2=PhotoImage(file="gov2.png")
    gov1 = PhotoImage(file="gov1.png")
    l1 = Label(sc, image=gov2)
    l2 = Label(sc, image=gov1)
    f2=Frame(sc,bg="green",height=50)

    l3=Label(f1,bg="green")
    l4=Label(f1,bg="green")
    l5 = Label(f1,bg="green")
    b117 = Button(text="hi",image=k)
    b117.place(relx=0.9, rely=0.147)


    l3["text"]="Voter ID: "+item[1]
    l4["text"] = "Citizen ID Number: " + item[3]
    l5["text"] = "Name: " + item[0]

    p1 = PhotoImage(file="1.png")
    p2 = PhotoImage(file="2.png")
    p3 = PhotoImage(file="3.png")
    p4 = PhotoImage(file="4.png")
    p5 = PhotoImage(file="5.png")
    p6 = PhotoImage(file="6.png")
    p7 = PhotoImage(file="7.png")
    p8 = PhotoImage(file="8.png")
    p9 = PhotoImage(file="9.png")
    p10 = PhotoImage(file="10.png")
    p11 = PhotoImage(file="11.png")
    p12 = PhotoImage(file="12.png")
    p13 = PhotoImage(file="13.png")
    p14 = PhotoImage(file="14.png")
    p15 = PhotoImage(file="15.png")


    def ff1():
        global party
        b1["bg"]="red"
        party=1

    def ff2():
        global party
        b2["bg"]="red"
        party=2

    def ff3():
        global party
        b3["bg"]="red"
        party=3

    def ff4():
        global party
        party=4

    def ff5():
        global party
        party=5

    def ff6():
        global party
        party=6

    def f7():
        global party
        party=7

    def f8():
        global party
        party=8

    def f9():
        global party
        party=9

    def f10():
        global party
        party=10

    def f11():
        global party
        party=11

    def f12():
        global party
        party=12

    def f13():
        global party
        party=13

    def f14():
        global party
        party=14

    def f15():
        global party
        party=15


    def submit():
        global party
        msg=messagebox.askyesno(message="Are you sure want to continue?")
        if msg==True:
            client.sendvote(party)
            sc.destroy()
        else:
            pass






    b1=Button(f2,image=p1,command=ff1,highlightcolor="red")
    b2=Button(f2,image=p2,command=ff2,highlightcolor="red")
    b3=Button(f2,image=p3,command=ff3,highlightcolor="red")
    b4=Button(f2,image=p4,command=ff4)
    b5=Button(f2,image=p5,command=ff5)
    b6=Button(f2,image=p6,command=ff6)
    b7=Button(f2,image=p7,command=f7)
    b8=Button(f2,image=p8,command=f8)
    b9=Button(f2,image=p9,command=f9)
    b10=Button(f2,image=p10,command=f10)
    b11 = Button(f2, image=p11,command=f11)
    b12 = Button(f2, image=p12,command=f12)
    b13 = Button(f2, image=p13,command=f13)
    b14 = Button(f2, image=p14,command=f14)
    b15 = Button(f2, image=p15,command=f15)




    b1.grid(row=0,column=1,padx=20,pady=20)
    b2.grid(row=0,column=2,padx=20,pady=20)
    b3.grid(row=0,column=3,padx=20,pady=20)
    b4.grid(row=0,column=4,padx=20,pady=20)
    b5.grid(row=0,column=5,padx=20,pady=20)
    b6.grid(row=1,column=1,padx=20,pady=20)
    b7.grid(row=1,column=2,padx=20,pady=20)
    b8.grid(row=1,column=3,padx=20,pady=20)
    b9.grid(row=1,column=4,padx=20,pady=20)
    b10.grid(row=1,column=5,padx=20,pady=20)
    b11.grid(row=2, column=1, padx=20, pady=20)
    b12.grid(row=2, column=2, padx=20, pady=20)
    b13.grid(row=2, column=3, padx=20, pady=20)
    b14.grid(row=2, column=4, padx=20, pady=20)
    b15.grid(row=2, column=5, padx=20, pady=20)

    f4=Frame(sc,height=50,width=2000,bg="blue")
    sub=Button(sc,text="Submit",font={0},command=submit)


    l1.place(relx=0.92,rely=0.001)
    l2.place(relx=0.01, rely=0.01)
    f1.place(relx=0, rely=0.125)
    f2.place(relx=0.3, rely=0.3)
    l3.place(relx=0.01,rely=0.1)
    l4.place(relx=0.01, rely=0.4)
    l5.place(relx=0.01, rely=0.7)
    f4.place(relx=0,rely=0.87)
    sub.place(relx=0.71,rely=0.88)





    sc.mainloop()
# item=("jhj","jbj","jhbhn","hb")
# min(item)
###############db##########
import sqlite3
c = sqlite3.connect("info4.db",check_same_thread=False)

def write(temp):
    c = sqlite3.connect("info4.db",check_same_thread=False)
    c.execute(
        '''CREATE TABLE IF NOT EXISTS info4(usr text, eml text, phon text, cou text, gen char ,dob text, pw text,ph BlOB)''')
    c.execute("INSERT INTO info4 VALUES (?,?,?,?,?,?,?,?)", temp)
    c.commit()

def read(user,pas):
    tc = c.execute("SELECT usr,pw,eml,phon,cou,gen,dob,ph from info4")
    print("inside read")
    for item in tc:
        if item[0] == user:
            if item[1] == pas:
                print(item)
                return item
    c.close()
    return False

def vote(data):
    c = sqlite3.connect("votebox.db",check_same_thread=False)
    c.execute(
        '''CREATE TABLE IF NOT EXISTS votebox(a1 integer ,a2 integer,a3 integer,a4 integer,a5 integer,a6 integer,a7 integer,a8 integer,a9 integer,a10 integer,a11 integer,a12 integer,a13 integer,a14, integer,a15 integer )''')

    if int(data)==1:
          c.execute("INSERT INTO votebox(a1) VALUES (1)")
    elif int(data)==2:
        c.execute("INSERT INTO votebox(a2) VALUES (1)")
    elif int(data)==3:
        c.execute("INSERT INTO votebox(a3) VALUES (1)")
    elif int(data) == 4:
        c.execute("INSERT INTO votebox(a4) VALUES (1)")
    elif int(data) == 5:
        c.execute("INSERT INTO votebox(a5) VALUES (1)")
    elif int(data) == 6:
        c.execute("INSERT INTO votebox(a6) VALUES (1)")
    elif int(data) == 7:
        c.execute("INSERT INTO votebox(a7) VALUES (1)")
    elif int(data) == 8:
        c.execute("INSERT INTO votebox(a8) VALUES (1)")
    elif int(data) == 9:
        c.execute("INSERT INTO votebox(a9) VALUES (1)")
    elif int(data) == 10:
        c.execute("INSERT INTO votebox(a10) VALUES (1)")
    elif int(data) == 11:
        c.execute("INSERT INTO votebox(a11) VALUES (1)")
    elif int(data) == 12:
        c.execute("INSERT INTO votebox(a12) VALUES (1)")
    elif int(data) == 13:
        c.execute("INSERT INTO votebox(a13) VALUES (1)")
    elif int(data) == 14:
        c.execute("INSERT INTO votebox(a14) VALUES (1)")
    elif int(data) == 15:
        c.execute("INSERT INTO votebox(a15) VALUES (1)")

    c.commit()
    c.close()

###############client#####
import socket
import time
global result
from tkinter import messagebox

def send(temp):

    s = socket.socket()

    host = '192.168.100.32'

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
                break

            except:
                print("Sending")
                time.sleep(0.5)
                timing+=0.5
                if timing==20:
                    print("server time out. Please retry after moment.")
                    break

    sending(temp)


def recv(user,pas):

    s = socket.socket()

    host = '192.168.100.32'

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

            #     # try:
            #     #
            #     #
            #     # except:
            #     #     print("Error in receving")
            #
            #     break
            #
            # except:
            #     print("Sending")
            #     time.sleep(0.5)
            #     timing+=0.5
            #     if timing==20:
            #         print("server time out. Please retry after moment.")
            #         break

    sending(user, pas)

    return result

def sendvote(party):
    s = socket.socket()

    host = '192.168.100.32'

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
            temp = str("vt, " + "//a/" + str(party))
            s.send(str.encode(temp))
            messagebox.showinfo(message="Your candidate has been sent.")
            break
        s.close()
    sending(party)
###########server#######
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
        print("Sent")




def recv_data(conn):
    global address
    while 1:
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