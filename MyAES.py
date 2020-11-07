# xor elements of 2 byte objects
def byte_xor(ba1, ba2):
    return bytes([a ^ b for a, b in zip(ba1, ba2)])


def encrypt_decrypt_ecb(key, plaintext):
    nr_of_blocks = len(plaintext) // 16
    ciphertext = b''

    for i in range(nr_of_blocks):
        block = plaintext[i * 16:(i + 1) * 16]
        ciphertext += byte_xor(key, block)[0:16]

    remainder = len(plaintext) % 16
    if remainder > 0:
        block = plaintext[nr_of_blocks * 16: nr_of_blocks * 16 + remainder]
        ciphertext += byte_xor(key, block)

    return ciphertext


def encrypt_cfb(key, input_text, iv, is_encrypt=True):
    nr_of_blocks = len(input_text) // 16
    output_text = b''

    for i in range(nr_of_blocks):
        plain_current_block = input_text[i * 16:(i + 1) * 16]
        encrypted_iv = byte_xor(key, iv)
        output_text_block = byte_xor(encrypted_iv, plain_current_block)
        output_text += output_text_block[0:16]
        if is_encrypt:
            iv = output_text_block
        else:
            iv = plain_current_block

    remainder = len(input_text) % 16
    if remainder > 0:
        plain_current_block = input_text[nr_of_blocks * 16: nr_of_blocks * 16 + remainder]
        encrypted_iv = byte_xor(key, iv)
        output_text_block = byte_xor(encrypted_iv, plain_current_block)
        output_text += output_text_block[0:remainder]

    return output_text


def encrypt(algorithm, key, plaintext, iv="", is_encrypt=True):
    if algorithm.lower() == "ecb":
        return encrypt_decrypt_ecb(key, plaintext)
    elif algorithm.lower() == "cfb":
        if iv != "":
            return encrypt_cfb(key, plaintext, iv, is_encrypt)
        print("Error: iv parameter must be specified for cfb encryption.")
        return False
    else:
        print("Invalid encryption method; must be \'ecb\' or \'cfb\'")
        return False




