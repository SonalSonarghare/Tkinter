from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from subprocess import call
import mysql.connector as con
root = Tk()
root.geometry("950x500")


def login():
    db = con.connect(host='localhost', user='root', password='123456', database='student')
    c = db.cursor()
    un = User_Value.get()
    pw = Password_Value.get()

    c.execute("SELECT * FROM register WHERE Username='" + un + "' AND Password = '" + pw + "'")
    result = c.fetchone()
    if result:
        messagebox.showinfo("Success", "Login Successful")
        call(['python', "main.py"])
    else:
        messagebox.showerror("Error", "Invalid Login")



login_label = Label(root, text="Login", font="times 30 bold", foreground="Purple")
login_label.place(x=650, y=0)

User_label=Label(root,text="UserName",font="times 20 bold", foreground="Purple")
User_label.place(x=500,y=100)

Password_label=Label(root,text="Password",font="times 20 bold", foreground="Purple")
Password_label.place(x=500,y=200)

User_Value=StringVar()
Password_Value=StringVar()

User_Entry=Entry(root,textvariable=User_Value,font="times 20 bold", foreground="Purple")
User_Entry.place(x=630,y=100)

Password_Entry=Entry(root,textvariable=Password_Value,font="times 20 bold", foreground="Purple",show="*")
Password_Entry.place(x=630,y=200)

loginbtn=Button(root,text="Login",foreground="white",background="purple",font="times 20 bold",command=login)
loginbtn.place(x=700,y=300)
# Make sure the path to the image file is correct
image = ImageTk.PhotoImage(file="login_img.jpg")
# Create a label and set the image
image_label = Label(root, image=image)
image_label.place(x=0, y=0)

root.mainloop()
