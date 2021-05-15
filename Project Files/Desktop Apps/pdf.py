from tkinter import filedialog
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import portrait
dir=filedialog.askdirectory(title="open images")
sdir=filedialog.askdirectory(title="where to save")
print(sdir)
filename=str(sdir)+"/"+"generated_pdf.pdf"
c=canvas.Canvas(filename,pagesize=portrait(A4))
for file in os.listdir(dir):
    if file.endswith(".jpg"):
        file=dir+"/"+str(file)
        print(file)
        c.drawImage(file, 25, 180, width=550, height=500)
        c.showPage()
c.save()

