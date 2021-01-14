from tkinter import *
from password_generator import PasswordGenerator as pwgen
master=Tk()
master.title("Password Generator")



def gen():
    password=pwgen()
    password.minlength=8
    password.maxlength=15
    password.minuchars=2
    result=password.generate()
    pw.insert(0,result)
def delete1():
    pw.delete(0,END)

pw=Entry(master)
label1=Label(master,text="Welcome User!!",padx=5,pady=5,font=("roboto",18,"bold"))
button1=Button(master,text="Generate!!",command=gen,padx=40,pady=5)
button2=Button(master,text="Exit",command=master.quit,padx=58,pady=5)
button3=Button(master,text="Clear",command=delete1,padx=50,pady=5)


label1.grid(row=0,column=0)
pw.grid(row=1,column=0)
button1.grid(row=2,column=0)
button2.grid(row=3,column=0)
button3.grid(row=3,column=1)


master.mainloop()