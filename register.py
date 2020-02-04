from tkinter import *
import os

def login_virify() :
    username1 = username_virify.get()
    password1 = password_virify.get()

    username_entry1.delete(0,END)
    password_entry1.delete(0,END)


    list = os.listdir()

    username1 = username1+".txt"
    if username1 in list :
      with open(username1,"r")as file:
        virify=file.read().splitlines()
        if password1 in virify:
            Label(screen2, text="login success ", fg="green").pack()
        else:
            Label(screen2, text=" passwordERROR ", fg="red").pack()
    else :
        Label(screen2,text="user not found",fg="red").pack()


def register_user():
    username_info= username.get()
    firstname_info = firstname.get()
    name_info=name.get()
    password_info=password.get()
    confirmpassword_info=confirmpassword.get()
    E_mail_info=E_mail.get()


    with open(username_info+".txt", "w")as file:
        file.write(firstname_info+"\n")
        file.write(name_info+"\n")
        file.write(username_info+"\n")
        file.write(password_info+"\n")
        file.write(confirmpassword_info+"\n")
        file.write(E_mail_info+"\n")



    username_entry.delete(0, END)
    firstname_entry.delete(0,END)
    name_entry.delete(0, END)
    password_entry.delete(0,END)
    confirmpassword_entry.delete(0,END)
    E_mail_entry.delete(0,END)


    Label(screen1,text="").pack() 
    Label(screen1,text="registration success ",fg = "green").pack()








def login_screen():
    global screen2
    screen2 = Toplevel(screen)
    screen.minsize(300,250)         
    screen.maxsize(300,250)
    screen2.title("Login")
    screen2.geometry("300x250")
    global username_virify
    global password_virify
    global username_entry1
    global password_entry1
    username_virify = StringVar()
    password_virify = StringVar()
    Label(screen2, text="login", font=("Arial black", 20)).pack()
    Label(screen2, text="").pack()
    Label(screen2, text="user name", ).pack()
    username_entry1=  Entry(screen2, textvariable=username_virify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="passwords", ).pack()
    password_entry1 = Entry(screen2, textvariable=password_virify, show="*")
    password_entry1.pack()
    Button(screen2, text="login", height="2", width="20",command= login_virify).pack()


def register_screen():
 global screen1
 screen1 = Toplevel(screen)
 screen1.minsize(300,500)
 screen1.maxsize(300,500)
 screen1.title("Register")
 screen1.geometry("300x250")
 global username
 global firstname
 global name
 global E_mail
 global password
 global confirmpassword

 global firstname_entry
 global name_entry
 global E_mail_entry
 global password_entry
 global confirmpassword_entry
 global username_entry

 username=StringVar()
 firstname = StringVar()
 name=StringVar()
 password = StringVar()
 E_mail= StringVar()
 confirmpassword=StringVar()
 Label(screen1, text = "registration",font =("Arial black",20),height = "2", width = "30").pack()
 Label(screen1, text="first name",font =("Arial black",10)).pack()
 firstname_entry= Entry(screen1, textvariable=firstname)
 firstname_entry.pack()
 Label(screen1, text="name",font =("Arial black",10)).pack()
 name_entry= Entry(screen1, textvariable=name)
 name_entry.pack()
 Label(screen1, text="username",font =("Arial black",10)).pack()
 username_entry= Entry(screen1, textvariable=username)
 username_entry.pack()
 Label(screen1, text="E_mail",font =("Arial black",10)).pack()
 E_mail_entry = Entry(screen1, textvariable=E_mail)
 E_mail_entry.pack()
 Label(screen1, text="passwords",font =("Arial black",10)).pack()
 password_entry= Entry(screen1,textvariable=password,show="*")
 password_entry.pack()
 Label(screen1, text="confirm passwords",font =("Arial black",10),height="2").pack()
 confirmpassword_entry= Entry(screen1,textvariable=confirmpassword,show="*")
 confirmpassword_entry.pack()
 Label(screen1, text="").pack()
 Button(screen1, text="sing up",height="2",width="30", command=register_user).pack()
def main_screen():
 global screen
 screen = Tk()
 screen.minsize(300,250)
 screen.maxsize(300,250)
 screen.geometry("300x250")
 screen.title("login and sing up")
 Label(screen, text = "welcome", height="2",width="80",fg = "white",bg="gray",font = ("arial black",20) ).pack()
 Label(screen, text ="").pack()
 Button(screen, text ="login", width="20", height="2", command= login_screen ).pack()
 Label(screen,text="").pack()
 Button(screen, text = "sing up ",width="20",height="2",command=register_screen).pack()

 screen.mainloop()


main_screen()