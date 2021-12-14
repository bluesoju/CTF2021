from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

word='edinburgh'
passwords=['napier','test','password','foxtrot','123456','qwerty']
password='napier'
passw=''

if (len(sys.argv)>1):
	word=str(sys.argv[1])

if (len(sys.argv)>2):
	password=str(sys.argv[2])

plaintext=''

def isprintable(s, codec='utf8'):
    try: s.decode(codec)
    except UnicodeDecodeError: return False
    else: return True

def encrypt(plaintext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

ciphertext=[]

key = hashlib.sha256(password.encode()).digest()

print('\n=========Calculation====================')

print('Word: ',word)
print('Password: ',password)
print('Key ',binascii.hexlify(key))

plaintext = Padding.appendPadding(word,blocksize=Padding.AES_blocksize,mode='CMS')

ciphertext = ciphertext+ list(encrypt(plaintext.encode(),key,AES.MODE_ECB))
print('Cipher: ',binascii.hexlify(bytes(ciphertext)))

print('\n=========Bruce Force====================')

for passw in passwords:
  try:
    key = hashlib.sha256(passw.encode()).digest()
    plaintext = decrypt(bytes(ciphertext),key,AES.MODE_ECB)
    if (isprintable(plaintext)):
      p=Padding.removePadding(plaintext.decode(),mode='CMS')
      print('Plain text is ',p,' and password is ', passw)
  except:
    print('', end=' ')
