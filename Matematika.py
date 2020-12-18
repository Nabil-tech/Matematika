#!usr/bin/python2
# coding: UTF-8
# created   : NBL CODE
# date      : 18-12-2020
# file name : Matematika.py
# Comunity  : -
# ©NBL CODE All Right Reversed

# recode gk akan menjadikan mu seorang programmer
# jadi mikir dulu kalo mau recode
# hargai karya orang maka kau juga akan di hargai

from os import system as sistem
from time import sleep as waktu
from random import randint 
import sys

logoaink = """\033[40;1m
\033[37;1m[\033[41;1m Tools NBL CODE \033[00;1m\033[37;1m]
\033[31;1m[\033[43;1m\033[37;1m The Real Bang Jago \033[00;1m\033[31;1m]     


\033[31;1m███████████████████\033[31;1m ███╗░░██╗██████╗░██╗░░░░░
\033[31;1m███████████████████\033[31;1m ████╗░██║██╔══██╗██║░░░░░
\033[31;1m███████████████████\033[31;1m ██╔██╗██║██████╦╝██║░░░░░
\033[37;1m███████████████████\033[37;1m ██║╚████║██╔══██╗██║░░░░░
\033[37;1m███████████████████\033[37;1m ██║░╚███║██████╦╝███████╗
\033[37;1m███████████████████\033[37;1m ╚═╝░░╚══╝╚═════╝░╚══════╝
"""

# menu pilihan
def menu():
    sistem("clear")
    try:
        user = open('.user.txt', 'r').read()
    except IOError:
        username()
    sistem("clear")
    print logoaink
    print '\033[31;1m[\033[33;1m+\033[31;1m]'+36*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]'
    ngaran = open(".user.txt", "r")
    name = ngaran.readlines()
    print "\033[37;m{\033[32;m*\033[37;m} \033[34;1muser :\033[37;1m", name[0]
    ngaran.close()
    print '\033[31;1m[\033[33;1m+\033[31;1m]'+36*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]\n'
    print '           \033[37;1m**  \033[32;1mMatematika  \033[37;1m**\n'
    print '\033[37;1m[\033[32;1m01\033[37;1m] \033[34;1mPenjumlahan'
    print '\033[37;1m[\033[32;1m02\033[37;1m] \033[34;1mPengurangan'
    print '\033[37;1m[\033[32;1m03\033[37;1m] \033[34;1mPerkalian'
    print '\033[37;1m[\033[32;1m04\033[37;1m] \033[34;1mPembagian'
    print '\033[37;1m[\033[32;1m05\033[37;1m] \033[34;1mMean'
    print '\033[37;1m[\033[32;1m06\033[37;1m] \033[34;1mMedian'
    print ''
    print '\033[37;1m[\033[31;1mrm\033[37;1m] \033[34;1mHapus User'
    print '\033[37;1m[\033[31;1mrn\033[37;1m] \033[34;1mGanti Nama User'
    print '\033[37;1m[\033[31;1m00\033[37;1m] \033[34;1mKeluar'
    pilih_menu()

# pilih menu
def pilih_menu():
    pilih = raw_input("\n\033[32;1m=> \033[37;1m")
    if pilih == '1' or pilih == '01':
        penjumlahan()
    elif pilih == '2' or pilih == '02':
        pengurangan()
    elif pilih == '3' or pilih == '03':
        perkalian()
    elif pilih == '4' or pilih == '04':
        pembagian()
    elif pilih == '5' or pilih == '05':
        mean()
    elif pilih == '6' or pilih == '06':
        median()
    elif pilih == 'rm' or pilih == 'RM':
        hapusUser()
    elif pilih == 'rn' or pilih == 'RN':
        gantiUser()
    elif pilih == '0' or pilih == '00':
        sistem("clear")
        exit("\033[37;1m(\033[32;1m*\033[37;1m) Keluar dari aplikasi")

# penjumlahan
def penjumlahan():
    sistem("clear")
    print logoaink
    print "             \033[37;1m{\033[42;1mPenjumlahan\033[00;1m\033[37;1m}"
    print ''
    nilai_1 = int(input("\033[35;1mNilai ke 1 : \033[37;1m"))
    nilai_2 = int(input("\033[35;1mNilai ke 2 : \033[37;1m"))
    hasil = nilai_1 + nilai_2
    print "\033[35;1mHasil dari\033[37;1m", nilai_1,"\033[31;1m+\033[37;1m", nilai_2, "\033[32;1m=\033[37;1m", hasil
    print ''
    raw_input("\033[31;1m[<enter>]")
    menu()

# pengurangan
def pengurangan():
    sistem("clear")
    print logoaink
    print "             \033[37;1m{\033[42;1mPengurangan\033[00;1m\033[37;1m}"
    print ''
    nilai_1 = int(input("\033[35;1mNilai ke 1 : \033[37;1m"))
    nilai_2 = int(input("\033[35;1mNilai ke 2 : \033[37;1m"))
    hasil = nilai_1 - nilai_2
    print "\033[35;1mHasil dari\033[37;1m", nilai_1,"\033[31;1m-\033[37;1m", nilai_2, "\033[32;1m=\033[37;1m", hasil
    print ''
    raw_input("\033[31;1m[<enter>]")
    menu()

# perkalian
def perkalian():
    sistem("clear")
    print logoaink
    print "             \033[37;1m{\033[42;1mPerkalian\033[00;1m\033[37;1m}"
    print ''
    nilai_1 = int(input("\033[35;1mNilai ke 1 : \033[37;1m"))
    nilai_2 = int(input("\033[35;1mNilai ke 2 : \033[37;1m"))
    hasil = nilai_1 * nilai_2
    print "\033[35;1mHasil dari\033[37;1m", nilai_1,"\033[31;1mx\033[37;1m", nilai_2, "\033[32;1m=\033[37;1m", hasil
    print ''
    raw_input("\033[31;1m[<enter>]")
    menu()

# pembagian
def pembagian():
    sistem("clear")
    print logoaink
    print "             \033[37;1m{\033[42;1mPembagian\033[00;1m\033[37;1m}"
    print ''
    nilai_1 = int(input("\033[35;1mNilai ke 1 : \033[37;1m"))
    nilai_2 = int(input("\033[35;1mNilai ke 2 : \033[37;1m"))
    hasil = nilai_1 / nilai_2
    print "\033[35;1mHasil dari\033[37;1m", nilai_1,"\033[31;1m:\033[37;1m", nilai_2, "\033[32;1m=\033[37;1m", hasil
    print ''
    raw_input("\033[31;1m[<enter>]")
    menu()
    
# mean
def cariMean(a, n):
    sum = 0
    for i in range(0, n):
        sum += a[i]
        return float(sum / n)
    sorted(a)
    if n % 2 != 0:
        return float(a[n / 2])
    return float((a[int((n - 1) / 2)] + a[int(n / 2)]) / 2.0)
    mean()

def mean():
    sistem("clear")
    print logoaink
    print "             \033[37;1m{\033[42;1mMean\033[00;1m\033[37;1m}"
    print ''
    a = tuple(input("\033[34;1mMasukan nilai \033[32;1m=> \033[37;1m"))
    n = len(a)
    print "\033[34;1mnilai Mean nya \033[32;1m=\033[37;1m", cariMean(a, n)
    print ''
    raw_input("\033[31;1m[<enter>]")
    menu()

# median
def cariMedian(a, n):
    sorted(a)

    if n % 2 != 0:
        return float(a[n / 2])

    return float((a[int((n - 1) / 2)] +
                  a[int(n / 2)]) / 2.0)

def median():
    sistem("clear")
    print logoaink
    print "             \033[37;1m{\033[42;1mMedian\033[00;1m\033[37;1m}"
    print ''
    a = tuple(input("\033[34;1mMasukan nilai \033[32;1m=> \033[37;1m"))
    n = len(a)
    print "\033[34;1mnilai Median nya \033[32;1m=\033[37;1m", cariMedian(a, n)
    print ''
    raw_input("\033[31;1m[<enter>]")
    menu()

# registrasi
def username():
    sistem("clear")
    print logoaink
    nama = raw_input("\033[37;1m{\033[32;1m*\033[37;1m} \033[34;1m Masukan Nama Kamu : \033[37;1m")
    user = open(".user.txt", "w")
    user.write(nama)
    user.close()
    menu()
     
# hapus user 
def hapusUser():
    sistem("clear")
    ngaran = open(".user.txt", "r")
    name = ngaran.readlines()
    print "\033[34;1mMenghapus User :\033[37;1m", name[0]
    ngaran.close()
    sistem("rm -rf .user.txt")

# ganti user
def gantiUser():
    sistem("clear")
    print logoaink
    ngaran = open(".user.txt", "r")
    name = ngaran.readlines()
    print "\033[37;1m{\033[32;1m*\033[37;1m} \033[34;1mNama User :\033[37;1m", name[0]
    print 42*"\033[32;1m="
    ngaran.close()
    nama = raw_input("\033[37;1m{\033[32;1m*\033[37;1m}\033[34;1m Ganti Nama : \033[37;1m")
    sistem("rm -rf .user.txt")
    user = open(".user.txt", "w")
    user.write(nama)
    user.close()
    menu()
    
if __name__ == '__main__': 
    print logoaink
    menu()