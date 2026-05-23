from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)
nonce = get_random_bytes(12)

cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

with open('sample.jpg', 'rb') as file:
    data = file.read()

ciphertext, tag = cipher.encrypt_and_digest(data)

with open('encrypted.bin', 'wb') as enc:
    enc.write(ciphertext)

print('Archivo cifrado correctamente')
