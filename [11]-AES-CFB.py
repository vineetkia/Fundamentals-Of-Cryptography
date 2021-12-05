from Cryptodome import Random
from Cryptodome.Cipher import AES 
from Cryptodome.Util.Padding import pad
from Cryptodome.Protocol.KDF import PBKDF2

key = b'BFA32EE58B6F15267694EB56D8648204'
encryptionData = 'This is a secret message'

data = encryptionData.encode('utf-8')
cipher_encrypt = AES.new(key, AES.MODE_CFB)
ciphered_bytes = cipher_encrypt.encrypt(data)
print(ciphered_bytes)

iv = cipher_encrypt.iv
ciphered_data = ciphered_bytes

cipher_decrypt = AES.new(key, AES.MODE_CFB, iv=iv)
deciphered_bytes = cipher_decrypt.decrypt(ciphered_data)
decrypted_data = deciphered_bytes.decode('utf-8')
print(decrypted_data)
