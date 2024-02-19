# -*- coding: utf-8 -*-
from tkinter import *

window = Tk()
window.geometry('400x500')
window.title('Canvas')

choice=StringVar()

loc=LabelFrame()
loc2=LabelFrame()
loc3=LabelFrame()

radiocaesar=Radiobutton(loc3,text='Шифр Цезаря',variable=choice,value='Цезарь')
radioatbash=Radiobutton(loc3,text='Шифр Атбаш',variable=choice,value="Атбаш")

n1=Label(loc,text='Введите текст: ')
plaintextbox=Entry(loc)

n2=Label(loc,text='Введите ключ: ')
keybox=Entry(loc)

ciphername=Label(loc2,text='Шифр Цезаря')
ciphermessage=Label(loc2,text=' ')

button=Button(loc2,text='Зашифровать')



loc3.pack(fill=X)
loc.pack(fill=X)
loc2.pack(fill=X)

radiocaesar.pack()
radioatbash.pack()

n1.grid(column=0,row=0,padx=20,pady=10)
plaintextbox.grid(column=0,row=1,pady=10,padx=20)

n2.grid(column=1,row=0,padx=20,pady=10)
keybox.grid(column=1,row=1,padx=20,pady=10)

ciphername.pack()
ciphermessage.pack()

button.pack()

if __name__=='__main__':
    window.mainloop()