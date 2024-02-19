# -*- coding: utf-8 -*-

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet2='яюэьыъщшчцхфутсрпонмлкйизжёедгвба'


def caesar_encrypt(plaintext, key):
    ciphertext = ''
    for i in plaintext.lower():
        if i==' ':
            ciphertext+=i
        else:
            index = alphabet.find(i)
            new_index = index + key
            new_letter = alphabet[new_index%len(alphabet)]
            ciphertext += new_letter

    return ciphertext

def abdysh(plaintext):
    ciphertext = ''
    for i in plaintext.lower():
        if i==' ':
            ciphertext+=i
        else:
            index = alphabet.find(i)
            new_index = alphabet2[index]
            ciphertext += new_index

    return ciphertext

def vernama(plaintext):
    ciphertext = ''
    for i in plaintext.lower():
        if i==' ':
            ciphertext+=i
        else:
            index = alphabet.find(i)
            new_index = alphabet2[index]
            ciphertext += new_index

    return ciphertext

