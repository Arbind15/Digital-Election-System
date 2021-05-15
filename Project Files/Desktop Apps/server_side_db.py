import sqlite3
c = sqlite3.connect("voterlist.db",check_same_thread=False)

def write(temp):
    c = sqlite3.connect("voterlist.db",check_same_thread=False)
    c.execute(
        '''CREATE TABLE IF NOT EXISTS voterlist(usr text, eml text, phon text, cou text, gen char ,dob text, pw text,ph BlOB,cid text,vid integer,vtsta text)''')
    tc = c.execute("SELECT cid from voterlist")
    c.commit()

    flag="yes"
    for item in tc:
        if str(item[0]) == str(temp[8]):
            flag = "not"
            result="not"
            return result

    if flag == "yes":
        c = sqlite3.connect("voterlist.db", check_same_thread=False)
        c.execute(
            '''CREATE TABLE IF NOT EXISTS voterlist(usr text, eml text, phon text, cou text, gen char ,dob text, pw text,ph BlOB,cid text,vid integer,vtsta text )''')
        c.execute("INSERT INTO voterlist VALUES (?,?,?,?,?,?,?,?,?,?,?)",temp)
        c.commit()
        result="yes"
        return result


def read(user,pas):
    tc = c.execute("SELECT usr,pw,eml,phon,cou,gen,dob,ph,cid,vid,vtsta from voterlist")
    print("inside read")
    for item in tc:
        if item[0] == user:
            if str(item[9]) == str(pas):
                print(item)
                return item
    c.commit()
    return False

def vote(data):

    data,vid=str(data).split("vid")
    c1 = sqlite3.connect("voterlist.db", check_same_thread=False)
    v="vote"
    temp=(v,vid,)
    c1.execute("UPDATE voterlist set vtsta=? where vid=?",temp)
    c1.commit()
    print(data,vid)

    c = sqlite3.connect("votebox.db",check_same_thread=False)
    c.execute(
        '''CREATE TABLE IF NOT EXISTS votebox(a1 integer ,a2 integer,a3 integer,a4 integer,a5 integer,a6 integer,a7 integer,a8 integer,a9 integer,a10 integer,a11 integer,a12 integer,a13 integer,a14,a15 integer )''')

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
