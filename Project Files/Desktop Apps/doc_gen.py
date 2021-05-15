from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import portrait
from reportlab.platypus import Image,paragraph
from reportlab.lib import colors
from reportlab.graphics import shapes,renderPDF
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code93


def pdf(data,loc,selfil):

    filename=str(loc)+"/"+str(data[0])+"_election_.pdf"
    c=canvas.Canvas(filename,pagesize=portrait(A4))
    c.drawInlineImage("gov1.png",20,740,width=None,height=None)
    c.drawInlineImage("gov2.png", 460, 740, width=None, height=None)
    #c.setFont('Times-Bold', 18,leading=0)
    c.drawString(250, 675, "Confidential ! ")
    c.rect(20,430,545,230)
    vid="Voter ID: "+str(data[9])
    c.drawString(35,640,vid)
    cid="Citizenship ID Number: "+str(data[8])
    c.drawString(35, 625,cid)
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
    bar=code93.Extended93(str(data[9]))
    # bar.barHeight=50
    # bar.barWidth=100
    bar.drawOn(c,440,500)




    print("dd")
    c.save()
