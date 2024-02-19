# -*- coding: utf-8 -*-
import interface
from Ciphers import caesar_encrypt
from Ciphers import abdysh

def change_cipher():
    global currentcipher
    currentcipher=interface.choice.get()
    if currentcipher=='Цезарь':
        interface.ciphername.config(text=f"Зашифровано шифром '{currentcipher}'")
        interface.keybox.config(state='normal')
    else:
        interface.ciphername.config(text=f"Зашифровано шифром '{currentcipher}'")
        interface.keybox.config(state='disabled')

interface.radiocaesar.config(command=change_cipher)
interface.radioatbash.config(command=change_cipher)

interface.choice.set('Атбаш')

change_cipher()

def encrypt():
    plaintext=interface.plaintextbox.get()
    if currentcipher=='Цезарь':
        key=int(interface.keybox.get())
        interface.ciphermessage.config(text=caesar_encrypt(plaintext,key))
    else:
        interface.ciphermessage.config(text=abdysh(plaintext))

interface.button.config(command=encrypt)

interface.window.mainloop()