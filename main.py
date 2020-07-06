#!/usr/bin/env python

import time
import requests
import keyboard
from random import choice, randint

line = "___________"

### Nik-name
minLen = 4
maxLen = 9

vowels = ('a', 'e', 'i', 'o', 'u', 'y')
consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z', 'sh', 'zh', 'ch', 'kh', 'th')

vowelsFirst = bool(randint(0, 1))
result = ""

for i in range(0, randint(minLen, maxLen)):
    isEven = i % 2 == 0
    if (vowelsFirst and isEven) or (not vowelsFirst and not isEven):
        result += choice(vowels)
    else:
        result += choice(consonants)

print("\nNik: "+result.title()+'\n'+line+'\n')
###

### Mail
email = ''
key = ''

name = result+str(randint(1977, 2004))
url = "https://post-shift.ru/api.php?action=new&name="+name
response = requests.get(url).text

response = response.split()
email = response[1]
key = response[3]

print("Email: "+email+'\n'+line+'\n')
print("Key: "+key)
###

### Passwd
longPasswd = randint(13, 15)

chars = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passwd = ''

for i in range(longPasswd): passwd += choice(chars)
print("Password: "+passwd+'\n'+line+'\n')
###

### Letter

print("Expect an email. The mail's lifetime is 10 minutes. \n - Press \"Ctrl + E\" to exit...")

# If you want to receive emails in Russian, add the "base64=decode" parameter
url =  "https://post-shift.ru/api.php?action=getmail&key="+key+"&cut=html&forced=1&id=1"

while True:
    response = requests.get(url).text
    if response != "Error: Letter not found.":
        print(line+'\n'*2+"Letter: "+response+'\n'+line+'\n')
        break
    if keyboard.is_pressed('Ctrl + E'):
        if response == "Error: Letter not found.":
            print(line+'\n'*2+"Letter not found!"+'\n'+line+'\n')
        else:
            print("Bye bye!"+'\n'+line+'\n')
        break

url = "https://post-shift.ru/api.php?action=delete&key="+key
response = requests.get(url).text
print("The email is deleted("+response+")"+'\n'+line+'\n')
###