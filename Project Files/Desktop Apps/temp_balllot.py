from tkinter import *
import os
import base64
from PIL import ImageTk,Image
from tkinter import messagebox
import client
import time
from ttkthemes import ThemedTk
from tkinter import ttk
import threading

def min(item):
    global party

    scc = ThemedTk(theme="arc")
    scc.title("ballot_page")
    scc.attributes('-fullscreen', True)
    scc.iconbitmap("gov2.ico")


    f1 =Frame(scc, height=123, width=2000,bg="#8fb7f7")
    c = Canvas(f1, width=120, height=100)

    def counter():
        tim = 30
        while 1:

            la=Label(scc,fg="red",font="10")
            timeformat = "Time remain: 00:{:02d}".format(tim)
            la["text"] = timeformat
            time.sleep(1)
            tim-=1
            la.place(relx=0.45,rely=0.08)
            if tim==-1:
                messagebox.askokcancel(message="Time Expired!\nPlease try later.")
                scc.destroy()








    th=threading.Thread(target=counter)
    th.daemon=True
    th.start()


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
    l1 = Label(scc, image=gov2)
    l2 =Label(scc, image=gov1)
    f2=Frame(scc,height=1000,width=1000,bg="#8fb7f7")

    l3=Label(f1,bg="#8fb7f7")
    l4=Label(f1,bg="#8fb7f7")
    l5 = Label(f1,bg="#8fb7f7")
    b117 = Button(image=k,bg="#8fb7f7")
    b117.place(relx=0.9, rely=0.135)


    l3["text"]="Voter ID: "+str(item[9])
    l4["text"] = "Citizen ID Number: " + str(item[8])
    l5["text"] = "Name: " + item[0]
    l6=Label(scc,fg="red",font="10")
    l6["text"] = "Party Selected: None"

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


    def ff1(*args):
        global party
        party = 1
        l6["text"]="Party Selected: "+str("Bibeksheel Sajha Party ")


    def ff2(*args):
        global party
        party = 2
        l6["text"]="Party Selected: "+str("Federal Socialist Forum")


    def ff3(*args):
        global party
        party = 3
        l6["text"]="Party Selected: "+str("Rastriya Janamorcha")


    def ff4(*args):
        global party
        party=4
        l6["text"] = "Party Selected: " + str("Rastriya Prajatantra Party ")

    def ff5(*args):
        global party
        party=5
        l6["text"] = "Party Selected: " + str("Naya Shakti Party")

    def ff6(*args):
        global party
        party=6
        l6["text"] = "Party Selected: " + str("Bahujan Shakti Party ")

    def f7():
        global party
        party=7
        l6["text"] = "Party Selected: " + str("Communist Party of Nepal (Marxist–Leninist)")

    def f8():
        global party
        party=8
        l6["text"] = "Party Selected: " + str("Communist Party of Nepal (Unified Marxist–Leninist)")

    def f9():
        global party
        party=9
        l6["text"] = "Party Selected: " + str("Nepal Pariwar Dal ")

    def f10():
        global party
        party=10
        l6["text"] = "Party Selected: " + str("Nepal Federal Socialist Party ")

    def f11():
        global party
        party=11
        l6["text"] = "Party Selected: " + str("Nepali Congress  ")

    def f12():
        global party
        party=12
        l6["text"] = "Party Selected: " + str("Nepali Janata Dal")

    def f13():
        global party
        party=13
        l6["text"] = "Party Selected: " + str("Rastriya Janamukti Party")


    def f14():
        global party
        party=14
        l6["text"] = "Party Selected: " + str("Rastriya Janata Party ")

    def f15():
        global party
        party=15
        l6["text"] = "Party Selected: " + str("Rastriya Prajatantra Party (United) ")


    def submit():
        try:
            global party
            msg=messagebox.askyesno(message="Are you sure want to continue?")
            if msg==True:
                client.sendvote(party,item)
                os.remove("n.png")
                scc.destroy()
            else:
                pass
        except NameError:
            messagebox.showinfo(message="One candidate must be selected.")
            pass






    b1=ttk.Button(f2,image=p1)
    b1.bind("<Button-1>",ff1)
    b2=ttk.Button(f2,image=p2)
    b2.bind("<Button-1>", ff2)
    b3=ttk.Button(f2,image=p3)
    b3.bind("<Button-1>", ff3)
    b4=ttk.Button(f2,image=p4,command=ff4)
    b5=ttk.Button(f2,image=p5,command=ff5)
    b6=ttk.Button(f2,image=p6,command=ff6)
    b7=ttk.Button(f2,image=p7,command=f7)
    b8=ttk.Button(f2,image=p8,command=f8)
    b9=ttk.Button(f2,image=p9,command=f9)
    b10=ttk.Button(f2,image=p10,command=f10)
    b11 = ttk.Button(f2, image=p11,command=f11)
    b12 = ttk.Button(f2, image=p12,command=f12)
    b13 = ttk.Button(f2, image=p13,command=f13)
    b14 = ttk.Button(f2, image=p14,command=f14)
    b15 = ttk.Button(f2, image=p15,command=f15)




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

    f4=Frame(scc,height=50,width=2000,bg="#8fb7f7")
    sub=ttk.Button(scc,text="Submit",command=submit)


    l1.place(relx=0.92,rely=0.001)
    l2.place(relx=0.01, rely=0.01)
    f1.place(relx=0, rely=0.125)
    f2.place(relx=0.24, rely=0.3)
    l4.place(relx=0.02,rely=0.1)
    l3.place(relx=0.047, rely=0.25)
    l5.place(relx=0.052, rely=0.4)
    l6.place(relx=0.24, rely=0.837)
    f4.place(relx=0,rely=0.87)
    sub.place(relx=0.71,rely=0.88)





    scc.mainloop()
# item=("jhj","jbj","jhbhn","hb")
# min(item)
