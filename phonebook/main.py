from tkinter import *
import datetime
from mypeople import People


date = datetime.datetime.now().date()
date = str(date)


class Application(object):
    def __init__(self,master):
        self.master =master

        #frames
        self.top =Frame(master,height=250,bg='white')
        self.top.pack(fill=X)

        self.bottom=Frame(master,height=500,bg='#0da3cc')
        self.bottom.pack(fill=X)

        #top frame design

        self.top_image =PhotoImage(file='icons/phonebook.png')
        self.top_image_label =Label(self.top,image=self.top_image,bg ='white')
        self.top_image_label.place(x=100,y=5)

        self.heading =Label(self.top,text ='My Phonebook App',
                            font ='arial 15 bold',bg ='white',fg ='#0da3cc')
        self.heading.place(x=250,y=20)

        self.date_lbl = Label(self.top,text =date,
                              bg='white')

        self.date_lbl.place(x=650,y=5)

        #button1 = view people
        self.viewButton = Button(self.bottom,text = "  My People  ",
                                 fg= '#0da3cc',bg ='white' ,font = "arial 12 bold",
                                 command =self.my_people)
        self.viewButton.place(x=300,y=80)
        #button_2 = add people
        #self.addButton = Button(self.bottom, text=" Add People",
         #                       fg= '#0da3cc',bg ='white' ,font="arial 12 bold")
        #self.addButton.place(x=300, y=140)

        #button_3 = about_us
        self.aboutButton = Button(self.bottom, text="  About Us   ",
                                  fg= '#0da3cc',bg ='white' ,font="arial 12 bold")
        self.aboutButton.place(x=300, y=140)


    def my_people(self):
        people = People()



def main():
    root =Tk()
    app=Application(root)
    root.title("Phonebook")
    root.geometry('750x650+350+200')
    root.resizable(False,False)
    root.mainloop()

if __name__ == '__main__':
    main()
