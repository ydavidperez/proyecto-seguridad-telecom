from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

with open('public.pem', 'wb') as pub:
    pub.write(public_key)

with open('private.pem', 'wb') as prv:
    prv.write(private_key)

cipher = PKCS1_OAEP.new(RSA.import_key(public_key))

message = b'clave-aes-segura'

ciphertext = cipher.encrypt(message)

print('Clave cifrada con RSA')
