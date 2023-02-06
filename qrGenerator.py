from tkinter import *
import qrcode
from tkinter import messagebox
from tkinter import filedialog
import os
from tkinter.ttk import Combobox

root= Tk()

root.title("Qr Generator")
root.geometry("1000x550")
root.config(bg="#eda929")
root.resizable(False,False)


def clear():
    title.set('')
    entry.set('')
    
    
def generate():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save("Qrcode/"+str(name)+".png")
    
    global Image
    Image=PhotoImage(file="Qrcode/"+str(name)+".png")
    Image_view.config(image=Image)
    
Image_view=Label(root,bg="#eda929")
Image_view.pack(padx=50,pady=10,side=RIGHT)
    
title=StringVar()
Label(root,text="TITLE :",fg="white",bg="#b7ea1f",font=15).place(x=50,y=170)
titre=Entry(root,textvariable=title,width=13,font="arial 15")
titre.place(x=50,y=220)

entry=StringVar()
Label(root,text="LINK :",fg="white",bg="#b7ea1f",font=15).place(x=50,y=280)
lien=Entry(root,textvariable=entry,width=28,font="arial 15")
lien.place(x=50,y=320)


Button(root,text="Generate",width=20,height=2,bg="#b7ea1f",fg="white",command=generate).place(x=120,y=360)
Button(root,text="Reset",width=20,height=2,bg="#b7ea1f",fg="white",command=clear).place(x=120,y=420)






Label(root,text="Copyright © 2023 -qrGenerator- Tous droits réservés",bg="#b7ea1f",fg="white").place(x=370,y=525)





















root.mainloop()

