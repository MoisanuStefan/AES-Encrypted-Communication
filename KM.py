import random
import socket
import os
from Crypto.Cipher import AES


K_prim = b'temaunulaborator'
IV = "saisprezecebiti1"
MSG_SIZE = 1024

#
# def get_random_string(length):
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for i in range(length))
#

def client_program():

    host = socket.gethostname()
    port = 6666
    client_socket = socket.socket()
    client_socket.connect((host, port))

    encryption_method = client_socket.recv(1024).decode()  # receive signal to generate key
    cipher = AES.new(K_prim, AES.MODE_ECB)
    #   key = get_random_string(16)
    key = os.urandom(16)     # generate random key using cryptographic library
    print("Randomly generated key: ", str(key))
    encrypted_k = cipher.encrypt(key)   # encrypt using AES library
    print("Ciphertext: ", encrypted_k)
    client_socket.send(encrypted_k)
    client_socket.close()


if __name__ == '__main__':
    client_program()
