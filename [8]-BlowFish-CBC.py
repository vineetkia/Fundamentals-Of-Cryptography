from Crypto.Cipher import Blowfish
from struct import pack

bs = Blowfish.block_size
key = b'An arbitrarily long key'
cipher = Blowfish.new(key, Blowfish.MODE_CBC)
plaintext = b'docendo discimus '
plen = bs - len(plaintext) % bs
padding = [plen]*plen
padding = pack('b'*plen, *padding)
msg = cipher.iv + cipher.encrypt(plaintext + padding)
