from Crypto.Cipher import AES
import os
from pwn import xor

key = 'a3e90e8701a3b2a68476a4c4c67d0783'
iv = os.urandom(16)		# IV must be 16 bytes too!
print (iv.encode('hex'))


cbc = AES.new(key, AES.MODE_CBC, iv)
ct1 = cbc.encrypt('a3e90e8701a3b2a68476a4c4c67d0783' * 2)
print (ct1.encode('hex'))

ecb = AES.new(key, AES.MODE_ECB)
block1 = ecb.encrypt(xor(iv, 'a3e90e8701a3b2a68476a4c4c67d0783'))
block2 = ecb.encrypt(xor(block1, 'a3e90e8701a3b2a68476a4c4c67d0783'))
ct2 = block1 + block2
print (ct2.encode('hex'))
