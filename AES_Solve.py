from Crypto.Cipher import AES

key = 'a3e90e8701a3b2a68476a4c4c67d0783' 			# Key must be either 16, 24, or 32 bytes
cipher = AES.new(key) 				# Default mode is ECB (same for DES)

ct1 = cipher.encrypt('c2a72a733fe98e28dbcef890d52d4292074d08abc8c280503fe25311bb7ea17f8865d8fadd5502d0e9c79cfd43dcd93e')	# AES encrypts 16 bytes at a time
print (repr(ct1))


ct2 = cipher.encrypt('c2a72a733fe98e28dbcef890d52d4292074d08abc8c280503fe25311bb7ea17f8865d8fadd5502d0e9c79cfd43dcd93e'*2)	# ECB mode at work
print (repr(ct2))
