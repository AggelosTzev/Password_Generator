from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from random import choice
import pyperclip

win = ThemedTk(theme='black')
win.configure(themebg='black')
win.title("Password Generator")

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()-_"

def Generate():
    Password_entry.delete(0, END)
    password_type = VAR.get()
    Length = int(length.get())

    password = ""
    c = ""

    if password_type == 8:
        c = letters
    elif password_type == 12:
        c = letters + numbers
    elif password_type == 16:
        c = letters + numbers + symbols

    for i in range(Length):
        character = choice(c)
        password += character

    Password_entry.insert(0, password)

def Encrypt():
    key = 4
    encrypted_pass = ""

    password_type = VAR.get()
    password = Password_entry.get()

    if password_type == 8:
        a = letters
        for i in range(len(password)):
            index = a.find(password[i])
            letter = (index + key) % len(a)
            encrypted_pass += a[letter]
    elif password_type == 12:
        a = letters + numbers
        for i in range(len(password)):
            index = a.find(password[i])
            letter = (index + key) % len(a)
            encrypted_pass += a[letter]
    elif password_type == 16:
        a = letters + numbers + symbols
        for i in range(len(password)):
            index = a.find(password[i])
            letter = (index + key) % len(a)
            encrypted_pass += a[letter]

    Password_entry.delete(0, END)
    Password_entry.insert(0, encrypted_pass)

def Copy():
    pyperclip.copy(Password_entry.get())


VAR = IntVar()

Title = ttk.Label(win, text="Password Generator", font=("Tahoma", 10))
Title.grid(row=0, column=1, columnspan=3)

Easy = ttk.Radiobutton(win, text="Easy", value=8, variable=VAR)
Easy.grid(row=2, column=4)

Medium = ttk.Radiobutton(win, text="Medium", value=12, variable=VAR)
Medium.grid(row=2, column=5)

Hard = ttk.Radiobutton(win, text="Hard", value=16, variable=VAR)
Hard.grid(row=2, column=6)

Length = ttk.Label(win, text="Length: ")
Length.grid(row=2, column=0)

length = ttk.Combobox(win)
length['values'] = (8, 12, 16)
length.grid(row=2, column=1, columnspan=1)

Password = ttk.Label(win, text="Password: ")
Password.grid(row=3, column=0)

Password_entry = ttk.Entry(win)
Password_entry.grid(row=3, column=1, columnspan=1)

Generator = ttk.Button(win, text="Generate", command=Generate)
Generator.grid(row=3, column=4)

Encrypt = ttk.Button(win, text="Encrypt", command=Encrypt)
Encrypt.grid(row=3, column=5)

Copy = ttk.Button(win, text="Copy", command=Copy)
Copy.grid(row=3, column=6)


win.mainloop()