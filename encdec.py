k = ''


class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[93m'
    WARNING = '\033[92m'
    FAIL = '\033[91m'
    # Formatting
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    # End colored text
    END = '\033[0m'

import re
import progressbar
import sys
import time
from tqdm import tqdm

def bashenc():
    s = input("Enter the message to Encrypt:")
    s1 = ""
    for k in s:
        s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))
    print("Encrypted message is:", s1)

def bashdec():
    s = input("Enter the message to Decrypt:")
    s1 = ""
    for k in s:
        s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))
    print("Decrypted message is:", s1)

def rotenc():
    s = ""
    j = None
    s = input("Enter ur string here to encrypt:")
    li = len(s)
    print(color.FAIL + "Encrypted string is:" + color.END, end="")
    time.sleep(4)
    while li != 0:
        for i in s:
            j = ord(i)
            if 97 <= j <= 109:
                j = j + 13
                # print(color.FAIL+"Encrypted string is:"+color.END,end="")
                print(chr(j), end="")
                li = li - 1
            elif 110 <= j <= 122:
                j = j - 13
                print(chr(j), end="")
                li = li - 1
            elif j == 32:
                print(chr(j), end="")
                li = li - 1

def rotdec():
    s = ""
    s = input("Enter the encrypted string to decrypt it:")
    li = len(s)
    print(color.FAIL + "Decrypted string is:" + color.END, end="")
    time.sleep(4)
    while li != 0:
        for i in s:
            j = ord(i)
            if 97 <= j <= 109:
                j = j + 13
                print(chr(j), end="")
                li = li - 1
            elif 110 <= j <= 122:
                j = j - 13
                print(chr(j), end="")
                li = li - 1
            elif j == 32:
                print(chr(j), end="")
                li = li - 1

def rot22enc():
    s = ""
    j = None
    s = input("Enter ur string here to encrypt:")
    li = len(s)
    print(color.FAIL + "Encrypted string is:" + color.END, end="")
    print("\n")
    time.sleep(4)
    while li != 0:
        for i in s:
            j = ord(i)
            if 97 <= j <= 100:
                j = j + 22
                # print(color.FAIL+"Encrypted string is:"+color.END,end="")
                print(chr(j), end="")
                li = li - 1
            elif 101 <= j <= 104:
                j = j - 4
                print(chr(j), end="")
                li = li - 1
            elif 105 <= j <= 108:
                j = j - 4
                print(chr(j), end="")
                li = li - 1
            elif 109 <= j <= 112:
                j = j - 4
                print(chr(j), end="")
                li = li - 1
            elif 113 <= j <= 116:
                j = j - 4
                print(chr(j), end="")
                li = li - 1
            elif 117 <= j <= 120:
                j = j - 4
                print(chr(j), end="")
                li = li - 1
            elif 121 <= j <= 122:
                j = j - 4
                print(chr(j), end="")
                li = li - 1
            elif j == 32:
                print(chr(j), end="")
                li = li - 1

def rot22dec():
    s = ""
    s = input("Enter the encrypted string to decrypt it:")
    li = len(s)
    print(color.FAIL + "\nDecrypted string is:" + color.END, end="")
    print("\n")
    time.sleep(4)
    while li != 0:
        for i in s:
            j = ord(i)
            if 119 <= j <= 122:
                j = j - 22
                print(chr(j), end="")
                li = li - 1
            elif 97 <= j <= 118:
                j = j + 4
                print(chr(j), end="")
                li = li - 1
            elif j == 32:
                print(chr(j), end="")
                li = li - 1

def simenc():
    s = ""
    s = input("Enter the string to encrypt here:")
    li = len(s)
    print(color.HEADER + "Encrypted string is:" + color.END, end="")
    print("\n")
    for i in s:
        k = ord(i)
        k = k + 1
        print(chr(k), end="")
        li = li - 1

def simdec():
    s = ""
    s = input("Enter the encrypted string here to decrypt it:")
    li = len(s)
    print(color.HEADER + "Decrypted string is" + color.END, end="")
    print("\n")
    for i in s:
        k = ord(i)
        k = k - 1
        print(chr(k), end="")
        li = li - 1

def cenc():
    s = "abcdefghijklmnopqrstuvwxyz"
    print("Current working string is:", s)
    k = input("Input a single word key u want to use for encryption:")
    i = ord(k)
    s = s.replace(k, '')
    s = k + s
    print("Now string is:", s)
    t = input("Enter the string to Encrypt here:")
    li = len(t)
    print("Encrypted string is:", end="")
    while li != 0:
        for n in t:
            j = ord(n)
            if j == ord('a'):
                j = i
                print(chr(j), end="")
                li = li - 1
            elif 'a' < n <= k:
                j = j - 1
                print(chr(j), end="")
                li = li - 1
            elif n > k:
                print(n, end="")
                li = li - 1
            elif ord(n) == 32:
                print(' ', end="")
                li = li - 1

def cdec():
    h = ""
    c = ''
    s = "abcdefghijklmonpqrstuvwxyz"
    t = input("Enter the Encrypted String to Decrypt it here:")
    k = input("Enter the key you used earlier during encryption:")
    s = s.replace(k, '')
    s = k + s
    i = ord(k)
    li = len(t)
    for j in t:
        p = ord(j)
        if j > k:
            print(j, end="")
        elif j < k:
            j = chr(ord(j) + 1)
            print(j, end="")
        elif j == k:
            print('a', end="")
        elif j == ' ':
            print(' ', end="")

def delay_print(s):
    for c in s:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.1)

def bar():
    progress = progressbar.ProgressBar()
    for __ in progress(range(25)):
        time.sleep(0.1)

print("This Script Can Encrypt Ur Message In a Different Manner So That No Third Person Can Read It!")
print("\n\n\n")
# choice=int(input(color.OKBLUE+"\nEnter 1 to start encryption and decryption process and 0 to exit the program:"+color.END))
'''if choice==0:
  delay_print(color.WARNING+"Thanks for using me!"+color.END)
  delay_print(color.FAIL+"Leave a Reply on cyberbot1502@gmail.com"+color.END)
  sys.exit(0)'''
bar()

def prnt():
    print("""            
              1. Encrypt the text
              2. Decrypt the text
              3. Exit from this method
                                          """)

while True:
    print("""
              1. Atbash Encryption
              2. Rot13
              3. Rot22
              4. Simple Encryption(add 1)
              5. caesar(with ur key) where ! denotes a single space 
              0. Exit The program 
                                              """)
    c = int(input("Your Choice-"))
    if c == 0:
        delay_print(color.WARNING + "Thanks for using me!" + color.END)
        delay_print(color.FAIL + "Leave a Reply on cyberbot1502@gmail.com" + color.END)
        sys.exit(0)

    if c == 1:

        while True:
            prnt()
            f = int(input("Enter your choice-"))
            if f == 1:
                bashenc()
            elif f == 2:
                bashdec()
            elif f == 3:
                break
            # ch = int(input("\nWant to do some more encryption-decryption task on Atbash then enter 2:"))
            '''if ch!=0:
prnt()

  elif c == 2:
        def prnt():
            print("""            
              1. Encrypt the text
              2. Decrypt the text
              3. Exit from this method
                                               """)'''

        while True:
            prnt()
            f = int(input("Enter your choice-"))
            if f == 1:
                rotenc()
            elif f == 2:
                rotdec()
            elif f == 3:
                break

    elif c == 3:

        cc = None
        while cc != 0:
            prnt()
            f = int(input("Enter your choice-"))
            if f == 1:
                rot22enc()
            elif f == 2:
                rot22dec()
            elif f == 3:
                break

    elif c == 4:

        while True:
            prnt()
            f = int(input("Enter your choice-"))
            if f == 1:
                simenc()
            elif f == 2:
                simdec()
            elif f == 3:
                break

    elif c == 5:

        while True:
            prnt()
            f = int(input("Enter your choice-"))
            if f == 1:
                cenc()
            elif f == 2:
                cdec()
            elif f == 3:
                break

