k=''
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
  delay_print("Atbash encryption method ready to launch!")
  s=""
  S=''
  print("\n")
  #s=input("Enter ur message here to encrypt:")
  j=int(input("Enter 1 if u want to encrypt only capital letters and 2 for encrypting small letters:"))
  if j==1:
   s=input("Enter ur message here to encrypt:")
   t = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V', 
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q', 
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L', 
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G', 
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A','@':'@',' ':' ','.':'.'} 
   for k in s:
    if k!=' ':
     S+=t[k]
    else:
     S+=' '
   delay_print(color.OKGREEN+"Encrypted messsage is:"+color.END)
   time.sleep(4)
   print(S)
  if j==2:
   s=input("Enter ur message here to encrypt:")
   t = {'a' : 'z', 'b' : 'y', 'c' : 'x', 'd' : 'w', 'e' : 'v', 
        'f' : 'u', 'g' : 't', 'h' : 's', 'i' : 'r', 'j' : 'q', 
        'k' : 'p', 'l' : 'o', 'm' : 'n', 'n' : 'm', 'o' : 'l', 
        'p' : 'k', 'q' : 'j', 'r' : 'i', 's' : 'h', 't' : 'g', 
        'u' : 'f', 'v' : 'e', 'w' : 'd', 'x' : 'c', 'y' : 'b', 'z' : 'a','@':'@',' ':' ','.':'.'}
   for k in s:
    if k!=' ':
     S+=t[k]
    else:
     S+=' '
   delay_print(color.OKGREEN+"Encrypted messsage is:"+color.END)
   time.sleep(4)
   print(S)



def bashdec(): 
 S=''
 j=int(input("Enter 1 to decrypt the Capital letters encrypted words:"))
 if j==1:
   s=input("Enter the message to decrypt:")
   t = {'Z' : 'A', 'Y' : 'B', 'X' : 'C', 'W' : 'D', 'V' : 'E', 
        'U' : 'F', 'T' : 'G', 'S' : 'H', 'R' : 'I', 'Q' : 'J', 
        'P' : 'K', 'O' : 'L', 'N' : 'M', 'M' : 'N', 'L' : 'O', 
        'K' : 'P', 'J' : 'Q', 'I' : 'R', 'H' : 'S', 'G' : 'T', 
        'F' : 'U', 'E' : 'V', 'D' : 'W', 'X' : 'C', 'B' : 'Y',
        'A' : 'Z','@':'@',' ':' ','.':'.'}
   for k in s:
    if k!=' ':
     S+=t[k]
    else:
     S+=' '
   delay_print(color.OKGREEN+"Decrypted messsage is:"+color.END)
   time.sleep(4)
   print(S)

 if j==2:
   s=input("Enter the message to decrypt:")
   t = {'z' : 'a', 'y' : 'b', 'x' : 'c', 'w' : 'd', 'v' : 'e', 
        'u' : 'f', 't' : 'g', 's' : 'h', 'r' : 'i', 'q' : 'j', 
        'p' : 'k', 'o' : 'l', 'n' : 'm', 'm' : 'n', 'l' : 'o', 
        'k' : 'p', 'j' : 'q', 'i' : 'r', 'h' : 's', 'g' : 't', 
        'f' : 'u', 'e' : 'v', 'd' : 'w', 'x' : 'c', 'b' : 'y',
        'a' : 'z','@':'@',' ':' ','.':'.'}
   for k in s:
    if k!=' ':
     S+=t[k]
    else:
     S+=' '
   delay_print(color.OKGREEN+"Decrypted messsage is:"+color.END)
   time.sleep(4)
   print(S)




def rotenc():
 s=""
 j=None
 s=input("Enter ur string here to encrypt:")
 li=len(s)
 print(color.FAIL+"Encrypted string is:"+color.END,end="")
 time.sleep(4)
 while li!=0:
  for i in s:
   j=ord(i)
   if j>=97 and j<=109:
    j=j+13
    #print(color.FAIL+"Encrypted string is:"+color.END,end="")
    print(chr(j),end="") 
    li=li-1
   elif j>=110 and j<=122:
    j=j-13
    print(chr(j),end="")
    li=li-1
   elif j==32:
    print(chr(j),end="")
    li=li-1

def rotdec():
 s=""
 s=input("Enter the encrypted string to decrypt it:")
 li=len(s)
 print(color.FAIL+"Decrypted string is:"+color.END,end="")
 time.sleep(4)
 while li!=0:
  for i in s:
   j=ord(i)
   if j>=97 and j<=109:
    j=j+13
    print(chr(j),end="")
    li=li-1
   elif j>=110 and j<=122:
    j=j-13
    print(chr(j),end="")
    li=li-1
   elif j==32:
    print(chr(j),end="")
    li=li-1


def rot22enc():
 s=""
 j=None
 s=input("Enter ur string here to encrypt:")
 li=len(s)
 print(color.FAIL+"Encrypted string is:"+color.END,end="")
 print("\n")
 time.sleep(4)
 while li!=0:
  for i in s:
   j=ord(i)
   if j>=97 and j<=100:
    j=j+22
    #print(color.FAIL+"Encrypted string is:"+color.END,end="")
    print(chr(j),end="") 
    li=li-1
   elif j>=101 and j<=104:
    j=j-4
    print(chr(j),end="")
    li=li-1
   elif j>=105 and j<=108:
    j=j-4
    print(chr(j),end="")
    li=li-1
   elif j>=109 and j<=112:
    j=j-4
    print(chr(j),end="")
    li=li-1
   elif j>=113 and j<=116:
    j=j-4
    print(chr(j),end="")
    li=li-1
   elif j>=117 and j<=120:
    j=j-4
    print(chr(j),end="")
    li=li-1
   elif j>=121 and j<=122:
    j=j-4
    print(chr(j),end="")
    li=li-1
   elif j==32:
    print(chr(j),end="")
    li=li-1

def rot22dec():
 s=""
 s=input("Enter the encrypted string to decrypt it:")
 li=len(s)
 print(color.FAIL+"\nDecrypted string is:"+color.END,end="")
 print("\n")
 time.sleep(4)
 while li!=0:
  for i in s:
   j=ord(i)
   if j>=119 and j<=122:
    j=j-22
    print(chr(j),end="")
    li=li-1
   elif j>=97 and j<=118:
    j=j+4
    print(chr(j),end="")
    li=li-1
   elif j==32:
    print(chr(j),end="")
    li=li-1
    
    

def simenc():
 s=""
 s=input("Enter the string to encrypt here:")
 li=len(s)
 print(color.HEADER+"Encrypted string is:"+color.END,end="")
 print("\n")
 for i in s:
  k=ord(i)
  k=k+1
  print(chr(k),end="")
  li=li-1

def simdec():
 s=""
 s=input("Enter the encrypted string here to decrypt it:")
 li=len(s)
 print(color.HEADER+"Decrypted string is"+color.END,end="")
 print("\n")
 for i in s:
  k=ord(i)
  k=k-1
  print(chr(k),end="")
  li=li-1

def cenc():
 s="abcdefghijklmnopqrstuvwxyz"
 print("Current working string is:",s)
 k=input("Input a single word key u want to use for encryption:")
 i=ord(k)
 s=s.replace(k,'')
 s=k+s
 print("Now string is:",s)
 t=input("Enter the string to Encrypt here:")
 li=len(t)
 print("Encrypted string is:",end="")
 while li!=0:
  for n in t:
   j=ord(n)
   if j==ord('a'):
    j=i
    print(chr(j),end="")
    li=li-1
   elif 'a' < n <= k:
    j=j-1
    print(chr(j),end="")
    li=li-1
   elif n>k:
    print(n,end="")
    li=li-1
   elif ord(n)==32:
    print(' ',end="")
    li=li-1


def cdec():
 h=""
 c=''
 s="abcdefghijklmonpqrstuvwxyz"
 t=input("Enter the Encrypted String to Decrypt it here:")
 k=input("Enter the key you used earlier during encryption:")
 s=s.replace(k,'')
 s=k+s
 i=ord(k)
 li=len(t)
 for j in t:
  p=ord(j)
  if j>k:
   print(j,end="")
  elif j<k:
   j=chr(ord(j)+1)
   print(j,end="") 
  elif j==k:
   print('a',end="")
  elif j==' ':
   print(' ',end="")

def delay_print(s):
 for c in s:
  print(c,end="")
  sys.stdout.flush()
  time.sleep(0.1)

def bar():
 progress = progressbar.ProgressBar()
 for i in progress(range(25)):
    time.sleep(0.1)

print("This Script Can Encrypt Ur Message In a Different Manner So That No Third Person Can Read It!")
print("\n\n\n")
#choice=int(input(color.OKBLUE+"\nEnter 1 to start encryption and decryption process and 0 to exit the program:"+color.END))
'''if choice==0:
  delay_print(color.WARNING+"Thanks for using me!"+color.END)
  delay_print(color.FAIL+"Leave a Reply on cyberbot1502@gmail.com"+color.END)
  sys.exit(0)'''
bar()

while True:
 print("""
              1. Atbash Encryption
              2. Rot13
              3. Rot22
              4. Simple Encryption(add 1)
              5. caesar(with ur key) where ! denotes a single space 
              6. Exit The program 
                                              """)
 c=int(input("Your Choice-"))
 if c==6:
  delay_print(color.WARNING+"Thanks for using me!"+color.END)
  delay_print(color.FAIL+"Leave a Reply on cyberbot1502@gmail.com"+color.END)
  sys.exit(0)

 if c==1:
  def prnt():
   print("""            
              1. Encrypt the text
              2. Decrypt the text
              3. Exit from this method
                                                  """)
  ch=None
  while ch!=0:
   prnt()
   f=int(input("Enter ur choice what to do now:"))
   if f==1:
    bashenc()
   if f==2:
    bashdec()
   ch=int(input("\nWant to do some more encryption-decryption task on Atbash then enter 2:"))
   '''if ch!=0:
    prnt()'''
   if ch==3:
    sys.exit(0)

 elif c==2:
   def pr():
      print("""            
              1. Encrypt the text
              2. Decrypt the text
              3. Exit from this method
                                               """)

   hc=None
   while hc!=0:
    pr()
    f=int(input("Enter ur choice what to do now:"))
    if f==1:
     rotenc()
    if f==2:
     rotdec()
    hc=int(input("\nTo do some more task in ROT13 enter 4 otherwise 0:"))
    print("\n")
    '''if hc!=0:
     pr()'''
    if hc==3:
     sys.exit(0)

 elif c==3:
  def p():
    print("""            
              1. Encrypt the text
              2. Decrypt the text
              3. Exit from this method

                                    """)
  cc=None
  while cc!=0:
   p()
   f=int(input("Enter ur choice what to do now:"))
   if f==1:
    rot22enc()
   if f==2:
    rot22dec()
   cc=int(input("\nTo do more task in ROT22 enter 4 otherwise 0:"))
   print("\n")
   '''if cc!=0:
    p()'''
   if cc==3:
    sys.exit(0)


 elif c==4:
  def t():
   print("""            
                  1. Encrypt the text
                  2. Decrypt the text
                  3. Exit from this method

                                        """)

  g=None
  while g!=0:
   t()
   f=int(input("Enter ur choice what to do now:"))
   if f==1:
    simenc()
   if f==2:
    simdec()
   g=int(input("\nTo do more task in Simple method enter 5 otherwise 0:"))
   '''if g!=0:
    f()'''
   if g==3:
    sys.exit(0)


 elif c==5:
  def f():
   print("""            
                  1. Encrypt the text
                  2. Decrypt the text
                  3. Exit from this method

                                        """)

  i=None
  while i!=0:
    f()
    g=int(input("Enter ur choice what to do now:"))
    if g==1:
     cenc()
    if g==2:
     cdec()
    i=int(input("\nTo do more task in caesor keyed enter 6 otherwise 0:"))
    '''if g!=0:
      f() '''
    if i==3:
     sys.exit(0)

