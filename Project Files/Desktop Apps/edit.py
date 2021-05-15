from tkinter import *
from tkinter import ttk
import sqlite3
from ttkthemes import ThemedTk
from tkinter import messagebox
nsc=ThemedTk(theme="Clearlooks")
tctzn = StringVar()
nsc.title("voter_list")
nsc.geometry("400x300")
nsc.resizable(False,False)
nsc.iconbitmap("gov2.ico")


def sreh(*args):
    global vid
    c = sqlite3.connect("voterlist.db", check_same_thread=False)
    tc = c.execute("SELECT usr,pw,eml,phon,cou,gen,dob,ph,cid,vid,vtsta from voterlist")
    l1 = ttk.Label(nsc, text="Enter Citizenship Number or Voter ID:")
    ectzn = Entry(nsc, textvariable=tctzn)
    l1.place(relx=0.05, rely=0.5)
    b1 = ttk.Button(nsc, text="Search",command=sreh)

    b1.place(relx=0.6, rely=0.58)
    ectzn.place(relx=0.559, rely=0.5)

    for item in tc:
        if str(item[8])==str(tctzn.get()) or str(item[9])==str(tctzn.get()):
            l1.destroy()
            ectzn.destroy()
            b1.destroy()
            la=ttk.Label(nsc)
            la["text"]="Information is:\n"+"Name:"+str(item[0])+"\nPhone Number: "+str(item[3])+"\nDate of birth: "+str(item[6])+"\nEmail: "+str(item[2])+"\nVote Status: "+str(item[10])
            la.place(relx=0.01,rely=0.1)
            vid=((item[8]),)

            bu1=ttk.Button(nsc,text="Delete",command=dele)
            bu1.place(relx=0.6, rely=0.58)
            bu2 = ttk.Button(nsc, text="Back", command=sreh)
            bu2.place(relx=0.5, rely=0.58)


sreh()


def dele():
    global vid
    print(vid)
    tc = sqlite3.connect("voterlist.db", check_same_thread=False)

    tc.execute("DELETE FROM voterlist  WHERE cid=(?)",vid)

    tc.commit()
    tc.close()
    messagebox.showinfo(message="Information deleted !")
    nsc.destroy()
nsc.mainloop()