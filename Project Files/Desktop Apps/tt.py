from tkinter import *
from tkinter import ttk, filedialog, messagebox
import sqlite3
import base64
import os



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
    tc = c.execute("SELECT usr,pw,eml,phon,cou,gen,dob,ph from info")
    for item in tc:
        if item[0] == te1.get():
            if item[1] == te2.get():
                f2.destroy()
                f5 = LabelFrame(sc, text=item[0], height=100, width=200, padx=50, pady=50, background="light green")
                l13 = Label(f5, text="Full Name: " + item[0], background="light green")
                l14 = Label(f5, text="Email: " + item[2], background="light green")
                l15 = Label(f5, text="Phone Number: " + item[3], background="light green")
                l16 = Label(f5, text="Country: " + item[4], background="light green")
                l17 = Label(f5, text="Gender: " + item[5], background="light green")
                l18 = Label(f5, text="DOB: " + item[6], background="light green")
                with open("np.png", "wb") as fptr:
                    fptr.write(base64.b64decode(item[7]))
                img1 = PhotoImage("np.png")
                l19 = Label(f5, image=img1)
                os.remove("np.png")

                f5.grid(column=3, row=3)
                l13.grid(column=2, row=2, sticky=W)
                l14.grid(column=2, row=3, sticky=W)
                l15.grid(column=2, row=4, sticky=W)
                l16.grid(column=2, row=5, sticky=W)
                l17.grid(column=2, row=6, sticky=W)
                l18.grid(column=2, row=7, sticky=W)
                l19.grid(column=3, row=1, sticky=E)

            else:
                tl2 = Label(f2, text="Wrong Password!!!", bg="light green")
                tl2.grid(column=3, row=3)
                b1.destroy()

                def fbr2():
                    e1.delete(0, END)
                    e2.delete(0, END)
                    tl2.destroy()
                    b1 = Button(f2, text="Login", command=fb1)
                    b1.grid(column=2, row=9)

                br = Button(f2, text="Retry", command=fbr2)
                br.grid(column=2, row=9)

        else:
            global txt
            txt = "No user found!!!"
            tl1 = Label(f2, text=txt, bg="light green")
            tl1.grid(column=3, row=2)
            b1.destroy()

            def fbr1():
                e1.delete(0, END)
                e2.delete(0, END)
                tl1.destroy()
                b1 = Button(f2, text="Login", command=fb1)
                b1.grid(column=2, row=9)

            br = Button(f2, text="Retry", command=fbr1)
            br.grid(column=2, row=9)


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
            ("jpeg files", "*.jpg"), ("all files", "*.*"), ("PNG files", "*.png")))
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
            global photo
            te5.set(te6.get() + te5.get())
            # print(te3.get(),"\t",te4.get(),"\t",te5.get(),"\n",tcon.get(),"\t",date.get(),"\t",tgen.get(),"\t",phdir.get(),"\t",te11.get(),"\t",te12.get(),"\t",selfil)
            temp = (te3.get(), te4.get(), te5.get(), tcon.get(), tgen.get(), date.get(), te11.get(), photo)
            c.execute("INSERT INTO info VALUES (?,?,?,?,?,?,?,?)", temp)
            c.commit()
            messagebox.showinfo(message="User added sucessfully!")

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


sc.mainloop()