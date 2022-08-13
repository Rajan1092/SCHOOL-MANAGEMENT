from tkinter import*
import tkinter.messagebox                               
import os                                               
from tkinter import ttk                                 
import random                                           
import time
import datetime

def main():
    root = Tk()
    app = Window_1(root)
    root.mainloop()


class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("School Management System")
        self.master.geometry('1350x750')
        self.master.config(bg="green")
        self.Frame = Frame(self.master, bg="green")
        self.Frame.pack()


        self.Username = StringVar()                             
        self.Password = StringVar()

        self.Lbl_Title = Label(self.Frame, text = 'Login Menu', font = ('arial',55,'bold'), bg = 'green', fg = 'Black')
        self.Lbl_Title.grid(row = 0, column = 0, columnspan =3, pady = 40)
        
        self.Login_Frame_1 = LabelFrame(self.Frame, width = 1350, height = 600, relief = 'ridge', bg = 'green', bd = 15,
                                        font = ('arial',20,'bold'))
        self.Login_Frame_1.grid(row = 1, column =0)
        self.Login_Frame_2 = LabelFrame(self.Frame, width = 1000, height = 600, relief = 'ridge',bg = 'green', bd = 15,
                                        font = ('arial',20,'bold'))
        self.Login_Frame_2.grid(row = 2, column = 0)


        #===================================================LABEL and ENTRIES=======================================================================
        self.Label_Username = Label(self.Login_Frame_1, text = 'Username', font = ('arial',20,'bold'), bg = 'green', bd = 20)
        self.Label_Username.grid(row = 0, column = 0)
        self.text_Username = Entry(self.Login_Frame_1, font = ('arial',20,'bold'), textvariable = self.Username)
        self.text_Username.grid(row = 0, column = 1, padx = 50)                       
        
        self.Label_Password = Label(self.Login_Frame_1, text = 'Password', font = ('arial',20,'bold'), bg = 'green', bd = 20)
        self.Label_Password.grid(row = 1, column = 0)
        self.text_Password = Entry(self.Login_Frame_1, font = ('arial',20,'bold'), show = '*', textvariable = self.Password)
        self.text_Password.grid(row = 1, column = 1) 
        
        
        #=============================================================BUTTONS=======================================================================
        self.btnLogin = Button(self.Login_Frame_2, text = 'Login', width = 10, font = ('airia',15,'bold'), command = self.Login)
        self.btnLogin.grid(row = 3, column = 0, padx = 8, pady = 20)

        self.btnReset = Button(self.Login_Frame_2, text = 'Reset', width = 10, font = ('airia',15,'bold'), command = self.Reset)
        self.btnReset.grid(row = 3, column = 1, padx = 8, pady = 20)

        self.btnExit = Button(self.Login_Frame_2, text = 'Exit', width = 10, font = ('airia',15,'bold'), command = self.Exit)
        self.btnExit.grid(row = 3, column = 2, padx = 8, pady = 20)


    def Login(self):
        u = (self.Username.get())
        p = (self.Password.get())

        if (u == str('admin') and p == str('admin')):
            self.__menu__()
        else:
            tkinter.messagebox.askyesno("Login","Error : Wrong Password")
            self.Username.set("")
            self.Password.set("")
         

        
    def Reset(self):
         self.Username.set("")
         self.Password.set("")
         self.text_Username.focus()


        
    def Exit(self):
        self.Exit = tkinter.messagebox.askokcancel("Login System", "Confirm if you want to Exit")
        if self.Exit > 0:
            self.master.destroy()
            return

    def __menu__(self):
        filename = 'Menu.py'
        os.system(filename)
        os.system('notepad'+filename)

    '''def new_window(self):
        self.new_Window = Toplevel(self.master)
        self.app = Window_2(self.new_Window)'''

class Window_2:
    def __init__(self, master):
        self.master = master
        self.master.title("School Managment System")
        self.master.geometry('1350x750')
        self.master.config(bg="green")
        self.Frame = Frame(self.master, bg="green")
        self.Frame.pack()

    

if __name__ == '__main__':
    main()                                              


