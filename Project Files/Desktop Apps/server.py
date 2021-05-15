from tkinter import *
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import threading
import temp_ser
from tkinter import messagebox
import _tkinter
import time
import sqlite3
import base64
sc=ThemedTk(theme="arc")
sc.minsize(300,300)
sc.resizable(False,False)
sc.title("server_status")
sc.iconbitmap("gov2.ico")
l=Label(sc,font={"10"},fg="green")
i=0
global tctzn
tctzn=StringVar
def staser():
    def th():
        i=0
        t1=threading.Thread(target=temp_ser.main)
        t1.daemon=True
        t1.start()

        b2.destroy()
        b1 = ttk.Button(sc, text="Stop Server", command=ext)
        b1.place(relx=0.38, rely=0.3)

        while 1:
            l2 =Label(sc,font={"10"},fg="green")
            l2["text"]=""
            l2.place(relx=0.38,rely=0.2)
            l["text"]="Server is running."
            l.place(relx=0.23,rely=0.1)
            l2["text"]=">"
            l2.place(relx=0.38,rely=0.2)
            time.sleep(0.5)
            l2["text"] = ">>"
            time.sleep(0.5)
            l2["text"] = ">>>"
            time.sleep(0.5)
            l2["text"] = ">>>>"
            l2.place(relx=0.38,rely=0.2)
            time.sleep(0.5)
            i+=1
            l2["text"] = ">>>>>"
            time.sleep(0.5)
            print(i)
            l2.place(relx=0.38,rely=0.2)
            l2.destroy()

    t=threading.Thread(target=th)
    t.daemon=True
    t.start()


def ext():
   exit()

def edit():
    tctzn=StringVar()
    nsc = ThemedTk(theme="arc")
    nsc=tk.Toplevel()
    nsc.title("voter_list")
    nsc.geometry("400x300")
    nsc.resizable(False,False)
    nsc.iconbitmap("gov2.ico")
    l1=ttk.Label(nsc,text="Enter Citizenship Number or Voter ID:")
    ectzn = Entry(nsc,textvariable=tctzn)
    l1.place(relx=0.05,rely=0.5)
    ectzn.place(relx=0.559, rely=0.49)

    def sreh(*args):
        global vid
        flag=""
        c = sqlite3.connect("voterlist.db", check_same_thread=False)
        tc = c.execute("SELECT usr,pw,eml,phon,cou,gen,dob,ph,cid,vid,vtsta from voterlist")
        print(str(tctzn.get()))
        print("dfd")
        i=0
        for item in tc:
            if str(item[8]) == str(tctzn.get()) or str(item[9]) == str(tctzn.get()):
                flag="True"
                l1.destroy()
                ectzn.destroy()
                b1.destroy()
                la = ttk.Label(nsc)
                la["text"] = "Information is:\n" + "Name:" + str(item[0]) + "\nPhone Number: " + str(
                    item[3]) + "\nDate of birth: " + str(item[6]) + "\nEmail: " + str(
                    item[2]) + "\nVote Status: " + str(item[10])
                la.place(relx=0.01, rely=0.1)
                vid = (int(item[9]),)

                def dele():
                    global vid
                    print(vid)
                    tc = sqlite3.connect("voterlist.db", check_same_thread=False)
                    tc.execute("""DELETE FROM voterlist  WHERE vid=(?)""", vid)
                    tc.commit()
                    tc.close()
                    la.destroy()
                    messagebox.showinfo(message="Information deleted !")
                    nsc.destroy()

                bu1 = ttk.Button(nsc, text="Delete", command=dele)
                bu1.place(relx=0.6, rely=0.58)
                bu2 = ttk.Button(nsc, text="Back", command=sreh)
                bu2.place(relx=0.32, rely=0.58)
        if flag!="True":
            messagebox.showinfo(message="No match found!")
            nsc.destroy()

    b1 = ttk.Button(nsc, text="Search", command=lambda:sreh(tctzn.get()))
    b1.place(relx=0.6, rely=0.58)
    nsc.mainloop()


def vvtl():
    nsc=ThemedTk(theme="arc")
    nsc.title("voter_list")
    w, h = nsc.winfo_screenwidth(), nsc.winfo_screenheight()
    nsc.geometry("%dx%d+0+0" % (w, h))
    nsc.iconbitmap("gov2.ico")
    c = sqlite3.connect("voterlist.db", check_same_thread=False)
    tc = c.execute("SELECT usr,pw,eml,phon,cou,gen,dob,ph,cid,vid,vtsta from voterlist")
    l=ttk.Label(nsc,text="Name:\t\t\tPassword:\t\tEmail:\t\t\t\tPhone Number:\t\tAddress:\t\t\tGender:\t\tDate of Birth:\t\tCitizenship ID Number:\tVoter ID Number:\t\tVote Status:")
    l.place(relx=0.01,rely=0.01)
    i=0.04
    for item in tc:
        l=ttk.Label(nsc,text=str(item[0])+"\t\t"+str(item[1])+"\t\t"+str(item[2])+"\t"+str(item[3])+"\t\t"+str(item[4])+"\t"+str(item[5])+"\t\t"+str(item[6])+"\t\t"+str(item[8])+"\t\t"+str(item[9])+"\t\t"+str(item[10]))
        l.place(relx=0.01,rely=i)
        i+=0.02
        print(item[0])
    nsc.mainloop()


def vrt():
    nsc = ThemedTk(theme="arc")
    nsc.title("vote_status")
    nsc.iconbitmap("gov2.ico")
    l=ttk.Label(nsc,text="Party Name:\t\t\tNumber of Vote",font={"10"})
    l.grid(row=0,column=0,sticky=W)

    l1=ttk.Label(nsc)
    l2 = ttk.Label(nsc)
    l3 = ttk.Label(nsc)
    l4 = ttk.Label(nsc)
    l5 = ttk.Label(nsc)
    l6 = ttk.Label(nsc)
    l7 = ttk.Label(nsc)
    l8 = ttk.Label(nsc)
    l9 = ttk.Label(nsc)
    l10 = ttk.Label(nsc)
    l11= ttk.Label(nsc)
    l12 = ttk.Label(nsc)
    l13 = ttk.Label(nsc)
    l14 = ttk.Label(nsc)
    l15 = ttk.Label(nsc)

    c = sqlite3.connect("votebox.db",check_same_thread=False)
    tc = c.execute("SELECT a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15 from votebox")
    a1=0
    a2=0
    a3=0
    a4=0
    a5=0
    a6=0
    a7=0
    a8=0
    a9=0
    a10=0
    a11=0
    a12=0
    a13=0
    a14=0
    a15=0
    for item in tc:
        if str(item[0])=="1":
            a1+=1
            l1["text"]="Bibeksheel Sajha Party "+"\t\t\t\t\t"+str(a1)
        if str(item[1])=="1":
            a2+=1
            l2["text"]="Federal Socialist Forum"+"\t\t\t\t"+str(a2)
        if str(item[2])=="1":
            a3+=1
            l3["text"]="Rastriya Janamorcha"+"\t\t\t\t"+str(a3)
        if str(item[3])=="1":
            a4+=1
            l4["text"]="Rastriya Prajatantra Party "+"\t\t\t"+str(a4)
        if str(item[4])=="1":
            a5+=1
            l5["text"]="Naya Shakti Party"+"\t\t\t\t"+str(a5)
        if str(item[5])=="1":
            a6+=1
            l6["text"]="Bahujan Shakti Party "+"\t\t\t\t"+str(a6)
        if str(item[6])=="1":
            a7+=1
            l7["text"]="Communist Party of Nepal (Marxist–Leninist)"+"\t\t"+str(a7)
        if str(item[7])=="1":
            a8+=1
            l8["text"]="Communist Party of Nepal (Unified Marxist–Leninist)"+"\t\t"+str(a8)
        if str(item[8])=="1":
            a9+=1
            l9["text"]="Nepal Pariwar Dal "+"\t\t\t\t\t"+str(a9)
        if str(item[9])=="1":
            a10+=1
            l10["text"]="Nepal Federal Socialist Party "+"\t\t\t"+str(a10)
        if str(item[10]) == "1":
            a11 += 1
            l11["text"] = "Nepali Congress  " + "\t\t\t\t\t" + str(a11)
        if str(item[11]) == "1":
            a12 += 1
            l12["text"] = "Nepali Janata Dal" + "\t\t\t\t\t" + str(a12)
        if str(item[12]) == "1":
            a13 += 1
            l13["text"] = "Rastriya Janamukti Party" + "\t\t\t\t" + str(a13)
        if str(item[13]) == "1":
            a14 += 1
            l14["text"] = "Rastriya Janata Party " + "\t\t\t\t" + str(a14)
        if str(item[14]) == "1":
            a15 += 1
            l15["text"] = "Rastriya Prajatantra Party (United) " + "\t\t" + str(a15)




    l1.grid(row=1,column=0,sticky=NSEW)
    l2.grid(row=2, column=0, sticky=NSEW)
    l3.grid(row=3, column=0, sticky=NSEW)
    l4.grid(row=4, column=0, sticky=NSEW)
    l5.grid(row=5, column=0, sticky=NSEW)
    l6.grid(row=6, column=0, sticky=NSEW)
    l7.grid(row=7, column=0, sticky=NSEW)
    l8.grid(row=8, column=0, sticky=NSEW)
    l9.grid(row=9, column=0, sticky=NSEW)
    l10.grid(row=10, column=0, sticky=NSEW)
    l11.grid(row=11, column=0, sticky=NSEW)
    l12.grid(row=12, column=0, sticky=NSEW)
    l13.grid(row=13, column=0, sticky=NSEW)
    l14.grid(row=14, column=0, sticky=NSEW)
    l15.grid(row=15, column=0, sticky=NSEW)
    nsc.mainloop()


def import_db():
    i=0
    data = []
    des = sqlite3.connect("D:\Documents\Python\Del_pro\db.sqlite3")
    tar = sqlite3.connect("voterlist.db")
    obj2=des.execute("SELECT * FROM login_voterlist")
    obj1 = des.execute("SELECT * FROM auth_user")
    tar.execute(
        '''CREATE TABLE IF NOT EXISTS voterlist(usr text, eml text, phon text, cou text, gen char ,dob text, pw text,ph BlOB,cid text,vid integer,vtsta text)''')
    for item1 in obj1:
        temp=[item1[4],item1[6],item1[1]]
        data.append(temp)

    for item2 in obj2:
        data[i].append(item2[1])
        data[i].append(item2[2])
        data[i].append(item2[3])
        data[i].append(item2[4])
        data[i].append(item2[6])
        data[i].append(item2[7])
        data[i].append(item2[8])
        data[i].append(item2[12])
        data[i].append(item2[11])
        i+=1

    for tem in data:
        print(tem[11])
        if str(tem[11])=="Approved":
            selfil="D:\Documents\Python\Del_pro\media/"+str(tem[9])
            with open(selfil, "rb") as fptr:
                photo = base64.b64encode(fptr.read())
            print(photo)
            tem1=(tem[0],tem[1],tem[3],tem[5],tem[6],tem[4],tem[2],photo,tem[7],tem[8],tem[10])
            print(tem1)
            tar.execute("INSERT INTO voterlist VALUES (?,?,?,?,?,?,?,?,?,?,?)", tem1)
    des.commit()
    tar.commit()
    print("DONE")

b2=ttk.Button(sc,text="Run Server",command=staser)
b2.place(relx=0.38,rely=0.3)

b3=ttk.Button(sc,text="View Voterlist",command=vvtl)
b3.place(relx=0.04,rely=0.6)

b4=ttk.Button(sc,text="View Result",command=vrt)
b4.place(relx=0.37,rely=0.6)

b4=ttk.Button(sc,text="Edit Database",command=edit)
b4.place(relx=0.67,rely=0.6)

b5=ttk.Button(sc,text="Import Database",command=import_db)
b5.place(relx=0.32,rely=0.72)





sc.mainloop()