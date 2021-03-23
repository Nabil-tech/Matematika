import requests
import shutil
import os
import json
import itertools
import threading
import time
import sys
G = '\033[92m'
Y = '\033[93m'
R = '\033[91m'
B = '\033[1m'
W = '\033[0m'

username = "Nabil" 
password = "NxCTzy4004" 

def login (user_name, pass_word) :
    if user_name != username and pass_word != password :
        hasil = False
    else :
        hasil = True

    return hasil

i=5
while i>=1:
    print (f'{G}link username & password:  {W}https://duit.cc/wzu4')
    userName_=input(f'{Y}masukan username anda :')
    password_=input(f'{Y}masukan password :')
    hasil=(login(userName_, password_))
    if hasil == True :
        print (f'{G}login user berhasil') 
        os.system('python univ.py')
    else :
        i-=1
        print('gagal login, sisa percobaan login adalah :', i )
              