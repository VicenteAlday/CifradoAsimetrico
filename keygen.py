import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import ast
import socket
from _thread import *
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)

publickey = key.publickey()


HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(bytes(str(publickey), 'utf-8'))
            #conn.sendall(key.publickey().exportKey(format='PEM', passphrase=None, pkcs=1))

decryptor = PKCS1_OAEP.new(key)
decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))

print("Contraseña desencriptada: ")
print(decrypted)
