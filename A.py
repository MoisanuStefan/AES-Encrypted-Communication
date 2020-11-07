import socket
import MyAES
from Crypto.Cipher import AES


K_prim = b'temaunulaborator'
IV = "saisprezecebiti1"
MSG_SIZE = 1024


def server_program():
    host = socket.gethostname()
    port = 6666

    server_socket = socket.socket()
    server_socket.bind((host, port))
    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    print("Waiting for B and KM to get online...\n")
    conn_b, address_b = server_socket.accept()
    print("Connection from: " + str(address_b))
    conn_km, address_km = server_socket.accept()
    print("Connection from: " + str(address_km))
    print("B and KM are here. Initiating communication...")

    encryption_method = input('Communicate with B using ECB or CFB? \n-> ')
    conn_b.send(encryption_method.lower().encode())  # tell B encryption method
    conn_km.send(encryption_method.encode())  # ask KM for encrypted key
    print("Requested key from KM")
    key_from_km = conn_km.recv(MSG_SIZE)  # wait for km to generate requested key
    conn_km.close()
    if not key_from_km:
        print("Received invalid message from KM. Terminating program...")
        exit(1)

    print("Key received from KM: ", key_from_km)
    cipher = AES.new(K_prim, AES.MODE_ECB)  # prepare cipher to decrypt key from km
    conn_b.send(key_from_km)  # send encrypted key to B
    print("Encrypted key sent to B.")
    decrypted_key = cipher.decrypt(key_from_km)  # decrypt key using algorithm from input
    print("Decrypted key: ", str(decrypted_key))
    print("Waiting for B to give go signal...")
    if conn_b.recv(MSG_SIZE).decode() == "go":

        print("Dialog initiated, send first message:")
        while True:
            msg_to_send = input('-> ')
            encrypted_message = MyAES.encrypt(encryption_method.lower(), decrypted_key, msg_to_send.encode(),
                                              IV.encode())  # encrypt using my own implementation for ECB or CFB
            conn_b.send(encrypted_message)  # send data to B
            msg_received = conn_b.recv(MSG_SIZE)
            if not msg_received:
                # if data is not received
                break
            decrypted_msg = MyAES.encrypt(encryption_method, decrypted_key, msg_received, IV.encode(), False).decode()  # decrypt using my own implementation for ECB or CFB
            print("->B: " + decrypted_msg)
            if decrypted_msg == "exit":
                print("B ended dialog.")
                break
    else:
        print("B is not ready to communicate.Terminating program")
        exit(2)

    conn_b.close()  # close the connection


if __name__ == '__main__':
    server_program()
