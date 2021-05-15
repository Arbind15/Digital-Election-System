from reportlab.pdfgen import canvas
import io
import os
from django.http import FileResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import portrait
from reportlab.platypus import Image,paragraph
from reportlab.lib import colors
from reportlab.graphics import shapes,renderPDF
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code93
from django.conf import settings


def pdf(request,data):
    buffer=io.BytesIO()
    filename=str(data[0])+"_election_.pdf"
    c=canvas.Canvas(buffer,pagesize=portrait(A4))
    media=settings.MEDIA_ROOT
    # os.open("/media/gov1.png",flags=os.O_RDONLY)
    c.drawInlineImage(media+"/gov1.png",20,740,width=None,height=None)
    c.drawInlineImage(media+"/gov2.png", 460, 740, width=None, height=None)
    #c.setFont('Times-Bold', 18,leading=0)
    c.drawInlineImage(media+"/conf.png", 215, 675, width=150, height=17)
    c.rect(20,430,545,230)
    vid="Voter ID: "+str(data[3])
    c.drawString(35,640,vid)
    cid="Citizenship ID Number: "+str(data[4])
    c.drawString(35, 625,cid)
    usr="Username: "+data[0]
    c.drawString(35, 610,usr)
    pw="Full Name: "+str(data[1])
    c.drawString(35, 595, pw)
    dob="Date of Birth: "+str(data[7])
    c.drawString(35, 580, dob)
    eml="Email: "+str(data[2])
    c.drawString(35, 565, eml)
    phon="Phone Number: "+str(data[5])
    c.drawString(35, 550, phon)
    add="Address: "+str(data[6])
    c.drawString(35, 535, add)
    c.drawString(35, 520, "Province: "+str(data[10]))
    c.drawString(35, 505, "Remark: " + str(data[9]))
    c.drawString(35, 490, "Vote Status: " + str(data[14]))
    c.drawInlineImage(media+"/"+str(data[11]), 475, 575, width=85, height=80)
    try:
        c.drawInlineImage(str(data[15]), 140, 500, width=20, height=20)
    except:
        pass
    bar=code93.Extended93(str(data[3]))
    # bar.barHeight=50
    # bar.barWidth=100
    bar.drawOn(c,472,545)
    c.drawInlineImage(media + "/" + str(data[12]), 170, 250, width=280, height=150)
    c.drawInlineImage(media + "/" + str(data[13]), 170, 50, width=280, height=150)

    c.showPage()
    c.save()
    buffer.seek(io.SEEK_SET)
    return FileResponse(buffer,as_attachment=True,filename=filename)
