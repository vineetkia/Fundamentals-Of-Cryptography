from Crypto.Cipher import DES3
from Crypto import Random

key = b'Sixteen byte key'
iv = Random.new().read(DES3.block_size)
cipher = DES3.new(key, DES3.MODE_OFB, iv)
plaintext = b'sona si latine loqueris '
msg = iv + cipher.encrypt(plaintext)
