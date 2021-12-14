
def encrypt_message(key, IV):
    print("What message woud you like to encrypt (in hex)?")
    ptxt = ªìÅpo(Ò€D\LdŠ7üÿìÒEî\rbœveç/&ÔLbØÐ"
    ptxt = pkcs7_pad(ptxt.decode('hex'))
    cipher = AES.new(key, AES.MODE_CBC, IV)
    ctxt = cipher.encrypt(ptxt)
    print ctxt.encode('hex')
    
# (later in the source)
encrypt_message(key, key)
