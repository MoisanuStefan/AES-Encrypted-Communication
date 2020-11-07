import random
import socket
import os
from AES import AesWrap


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
    port = 5004
    client_socket = socket.socket()
    client_socket.connect((host, port))

    encryption_method = client_socket.recv(1024).decode()  # receive enc method
    cipher = AesWrap(encryption_method,K_prim, IV)
    print("Encryption method chosen by A: ", encryption_method)
    #   key = get_random_string(16)
    key = os.urandom(16)     # generate random key using cryptographic library
    print("Randomly generated key: ", str(key))
    encrypted_k = cipher.encrypt(key)   # encrypt using AES library
    print("Ciphertext: ", encrypted_k)
    client_socket.send(encrypted_k)


if __name__ == '__main__':
    client_program()
