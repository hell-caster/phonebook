from tkinter import *
from addpeople import AddPeople
from display import DisplayPeople
import sqlite3

con = sqlite3.connect('database.db')
cur =con.cursor()

class People(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)

        self.geometry('750x750+600+200')
        self.title("My People")
        self.resizable(False,False)

        self.top = Frame(self, height=250, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#0da3cc')
        self.bottom.pack(fill=X)

        # top frame design

        self.top_image = PhotoImage(file='icons/programmer.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=100, y=5)

        self.heading = Label(self.top, text='My People',
                             font='arial 15 bold', bg='white', fg='#0da3cc')
        self.heading.place(x=150, y=20)

        self.scroll = Scrollbar(self.bottom,orient=VERTICAL)

        self.listBox = Listbox(self.bottom,width=50,height=25)
        self.listBox.grid(row=0,column=0,padx=(40,0))
        self.scroll.config(command=self.listBox.yview())
        self.listBox.config(yscrollcommand=self.scroll.set)

        self.scroll.grid(row=0,column=1,sticky=N+S)

        #Buttons
        btnadd = Button(self.bottom,text ="ADD",width =12,font ="arial 12 bold",command=self.add_people)
        btnadd.grid(row=0,column=2,padx=20,pady=10,sticky =N)

        #btnupdate = Button(self.bottom, text="UPDATE", width=12, font="arial 12 bold")
        #btnupdate.grid(row=0, column=2, padx=20, pady=50, sticky=N)

        btnDisplay = Button(self.bottom, text="DISPLAY", width=12, font="arial 12 bold",command=self.display_people)
        btnDisplay.grid(row=0, column=2, padx=20, pady=50, sticky=N)

    def add_people(self):
        add_page =AddPeople()

    def display_people(self):
        add_page =DisplayPeople()
