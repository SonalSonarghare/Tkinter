from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector as con
from subprocess import call
#creating a main window
root = Tk()

#Set the Initial Size of the window
root.geometry("1000x700")


#Database
def register():
    try:
        db = con.connect(host="localhost", user="root", password="123456", database="student",auth_plugin='mysql_native_password')
        c = db.cursor()

        Name = Name_Value.get()
        Gender = Gender_Value.get()
        Branch = Branch_Value.get()
        Phone = Phone_Value.get()
        Username = User_Value.get()
        Password = Password_Value.get()

        query = "INSERT INTO register (Name, Gender, Branch, Phone, Username, Password) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (Name, Gender, Branch, Phone, Username, Password)

        c.execute(query, values)
        db.commit()
        messagebox.showinfo('Success', 'Successfully Inserted')
        call(['python', "login.py"])
        root.destroy()  # Use self.root instead of root

    except Exception as e:
        messagebox.showinfo('Unsuccessful', f'Try Again: {e}')


# Creating a label with text "Registration" and specified font
registration_label = Label(root, text="Registration", font="times 20 bold",  foreground="blue")
registration_label.pack() # Packing the label to display it in the window

#Label
Name_label = Label(root , text="Name", font="times 15 bold")
Name_label.place(x=50,y=100)

Gender_label = Label(root , text="Gender", font="times 15 bold")
Gender_label.place(x=500,y=100)

Branch_label = Label(root , text="Branch", font="times 15 bold")
Branch_label.place(x=50,y=180)

Phone_label = Label(root , text="Phone No", font="times 15 bold")
Phone_label.place(x=500,y=180)

User_label = Label(root , text="Username", font="times 15 bold")
User_label.place(x=50,y=260)

Password_label = Label(root , text="Password", font="times 15 bold")
Password_label.place(x=500,y=260)

#Entry

Name_Value = StringVar()
Gender_Value = StringVar()
Branch_Value = StringVar(value="Select Branch")
Phone_Value = StringVar()
User_Value = StringVar()
Password_Value = StringVar()

NameEntry=Entry(root,textvariable=Name_Value,font="times 15 bold")
NameEntry.place(x=140,y=100)

GenderEntry1=Radiobutton(root,variable=Gender_Value,text='Male',value='male',font="times 12 bold")
GenderEntry1.place(x=590,y=100)

GenderEntry2=Radiobutton(root,variable=Gender_Value,text='Female',value='female',font="times 12 bold")
GenderEntry2.place(x=590,y=120)

branch=['Comps','IT','DS','AIML']
BranchEntry=ttk.Combobox(root,textvariable=Branch_Value,values=branch,font="times 12 bold",state="readonly")
BranchEntry.place(x=140,y=180)

PhoneEntry=Entry(root,textvariable=Phone_Value,font="times 15 bold")
PhoneEntry.place(x=590,y=180)

UserNameEntry=Entry(root,textvariable=User_Value,font="times 15 bold")
UserNameEntry.place(x=140,y=260)

PasswordEntry=Entry(root,textvariable=Password_Value,font="times 15 bold",show="*")
PasswordEntry.place(x=590,y=260)

#Button
Regbtn=Button(root,text="Register",bg="blue",fg="white",font="times 15 bold",command=register)
Regbtn.place(x=400,y=400)






# Running the Tkinter event loop
root.mainloop()