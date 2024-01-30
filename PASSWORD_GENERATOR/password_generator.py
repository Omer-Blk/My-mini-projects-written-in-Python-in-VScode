import random
from tkinter import *
from tkinter import messagebox
import pyperclip

gui = Tk()
gui.title('Parola Oluşturucu')
gui.geometry('250x200')
gui.resizable(0,0)

def process():
    length = int(string_pass.get())
     #characters of the password to be created
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special = ['@', '#', '$', '%', '&', '*']
    all = lower + upper + num + special
    ran = random.sample(all,length)
    password = "".join(ran)
    messagebox.showinfo('Sonuç', 'Parolanız {} \n\nŞifre Panoya Kopyalandı'.format(password))
    pyperclip.copy(password)

string_pass = StringVar()
label = Label(text="Parola Uzunluğu Girin").pack(pady=10)
txt = Entry(textvariable=string_pass).pack()
btn = Button(text="Oluştur", command=process).pack(pady=10)

gui.mainloop()
