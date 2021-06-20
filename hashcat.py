import os
import bcrypt
import socket
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import ast
from _thread import *

hashMode = input('Ingrese el modo de hash: ')
archivo = input('Ingrese (o arrastre) la direccion del archivo a hashear: ')
dicc1 = input('Ingrese la direccion del primer diccionario: ')
dicc2 = input('Ingrese la direccion del segundo diccionario: ')

os.system(f'cmd /k "hashcat.exe -m {hashMode} -a 0 {archivo} {dicc1} {dicc2} --force"')

archivo1 = open(r'C:\Users\Vicente\Desktop\hashcat\archivo1.txt', 'r').readlines()
bcrypted1 = open('bcrypted1.txt', 'w')
for x in archivo1:
    pass1 = x.strip().rsplit(':',1)[1]
    hashed1 = bcrypt.hashpw(b'pass1', bcrypt.gensalt())
    bcrypted1.write("%s\n" % hashed1.decode("utf-8"))
    print(pass1)
    print(hashed1)
bcrypted1.close()

archivo2 = open(r'C:\Users\Vicente\Desktop\hashcat\archivo2.txt', 'r').readlines()
bcrypted2 = open('bcrypted2.txt', 'w')
for x in archivo2:
    pass2 = x.strip().rsplit(':',1)[1]
    hashed2 = bcrypt.hashpw(b'pass2', bcrypt.gensalt())
    bcrypted2.write("%s\n" % hashed2.decode("utf-8"))
    print(pass2)
    print(hashed2)
bcrypted2.close()

archivo3 = open(r'C:\Users\Vicente\Desktop\hashcat\archivo3.txt', 'r').readlines()
bcrypted3 = open('bcrypted3.txt', 'w')
for x in archivo3:
    pass3 = x.strip().rsplit(':',1)[1]
    hashed3 = bcrypt.hashpw(b'pass3', bcrypt.gensalt())
    bcrypted3.write("%s\n" % hashed3.decode("utf-8"))
    print(pass3)
    print(hashed3)
bcrypted3.close()

archivo4 = open(r'C:\Users\Vicente\Desktop\hashcat\archivo4.txt', 'r').readlines()
bcrypted4 = open('bcrypted4.txt', 'w')
for x in archivo4:
    pass4 = x.strip().rsplit(':',1)[1]
    hashed4 = bcrypt.hashpw(b'pass4', bcrypt.gensalt())
    bcrypted4.write("%s\n" % hashed4.decode("utf-8"))
    print(pass4)
    print(hashed4)
bcrypted4.close()

archivo5 = open(r'C:\Users\Vicente\Desktop\hashcat\archivo5.txt', 'r').readlines()
bcrypted5 = open('bcrypted5.txt', 'w')
for x in archivo5:
    pass5 = x.strip().rsplit(':',1)[1]
    hashed5 = bcrypt.hashpw(b'pass5', bcrypt.gensalt())
    bcrypted5.write("%s\n" % hashed5.decode("utf-8"))
    print(pass5)
    print(hashed5)
bcrypted5.close()

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    publickey = s.recv(1024)
print('Received', repr(publickey))

pk = publickey.decode("utf-8")
print(pk)
encryptor = PKCS1_OAEP.new(repr(publickey))
encrypted = encryptor.encrypt(b'$2b$12$GQBItgpLESNJ0hWAMva.rOK/yvcrEQ9vAIaxUM5JxJPNhTUazG.XW') 

print(encrypted)
