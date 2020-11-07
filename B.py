import MyAES
import socket
from Crypto.Cipher import AES

go_msg = "go"
K_prim = b'temaunulaborator'
IV = "saisprezecebiti1"
MSG_SIZE = 1024


def client_program():
    host = socket.gethostname()
    port = 6666
    client_socket = socket.socket()
    client_socket.connect((host, port))

    encryption_method = client_socket.recv(MSG_SIZE).decode()  # receive enc method
    key_from_a = client_socket.recv(MSG_SIZE)  # receive encrypted key
    cipher = AES.new(K_prim, AES.MODE_ECB)  # prepare cipher for decryption

    decrypted_key = cipher.decrypt(key_from_a)  # decrypt the key using specified encryption method
    print("Received key from A and decrypted it using " + encryption_method.lower() + " algorithm: ", decrypted_key)
    client_socket.send(go_msg.encode())
    print("Go signal sent.")
    while True:
        msg_from_a = client_socket.recv(MSG_SIZE)  # receive encrypted msg
        if not msg_from_a:
            print("Communication terminated.")
            break

        decrypted_msg = MyAES.encrypt(encryption_method, decrypted_key, msg_from_a, IV.encode(), False).decode()
        print('->A: ' + decrypted_msg)
        if decrypted_msg == "exit":
            break
        msg_to_send = input("-> ")
        encrypted_msg = MyAES.encrypt(encryption_method, decrypted_key, msg_to_send.encode(), IV.encode())
        client_socket.send(encrypted_msg)

    client_socket.close()


if __name__ == '__main__':
    client_program()
