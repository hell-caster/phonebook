from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('database.db')
cur =con.cursor()
class AddPeople(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)

        self.geometry('750x750+600+200')
        self.title("Add People")
        self.resizable(False,False)

        self.top = Frame(self, height=250, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#0da3cc')
        self.bottom.pack(fill=X)

        # top frame design

        self.top_image = PhotoImage(file='icons/programmer.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=100, y=5)

        self.heading = Label(self.top, text='Add People',
                             font='arial 15 bold', bg='white', fg='#0da3cc')
        self.heading.place(x=150, y=20)

        #name
        self.label_name =Label(self.bottom,text ='Name',fg='white', bg='#7f7f7f')
        self.label_name.place(x=40,y=40)

        self.entry_name =Entry(self.bottom,width=30,bd=5)
        self.entry_name.insert(0,"Enter Name")
        self.entry_name.place(x=150,y=40)
        #suranme
        #self.label_surname = Label(self.bottom, text='SurName', fg='white', bg='#7f7f7f')
        #self.label_surname.place(x=40, y=80)

        #self.entry_surname = Entry(self.bottom, width=30, bd=5)
        #self.entry_surname.insert(0, "Enter SurName")
        #self.entry_surname.place(x=150, y=80)
        #phone
        self.label_phone = Label(self.bottom, text='Phone Number', fg='white', bg='#7f7f7f')
        self.label_phone.place(x=40, y=120)

        self.entry_phone = Entry(self.bottom, width=30, bd=5)
        self.entry_phone.insert(0, "Enter Phone Number")
        self.entry_phone.place(x=150, y=120)
        #email
        self.label_email = Label(self.bottom, text='Email', fg='white', bg='#7f7f7f')
        self.label_email.place(x=40, y=80)

        self.entry_email = Entry(self.bottom, width=30, bd=5)
        self.entry_email.insert(0, "Enter Email")
        self.entry_email.place(x=150, y=80)
        #address
        self.label_address = Label(self.bottom, text='Address', fg='white', bg='#7f7f7f')
        self.label_address.place(x=40, y=160)

        self.entry_address = Entry(self.bottom, width=30, bd=5)
        self.entry_address.insert(0, "Enter Address")
        self.entry_address.place(x=150, y=160)
        #button
        button = Button(self.bottom, text="Submit",
                                fg='#0da3cc', bg='white', font="arial 12 bold",command=self.add_people)
        button.place(x=200, y=250)

    def add_people(self):
        name =self.entry_name.get()
        phone =self.entry_phone.get()
        email =self.entry_email.get()
        address =self.entry_address.get()

        #print(name)

        if name and phone and email and address !="":
            #print("this function is running")

            try :
                query = "insert into 'addressbook' (person_name,person_email,person_phone,person_address) values(?,?,?,?)"
                cur.execute(query,(name,email,phone,address))
                #con = commit()
                messagebox.showinfo("Sucess","Contact added")

            except EXCEPTION as e:
                messagebox.showerror("Error",str(e))

        else :
            messagebox.showerror("Error","Fill all the details",icon='warning')

