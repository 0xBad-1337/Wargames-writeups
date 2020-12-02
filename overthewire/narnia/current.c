#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// gcc's variable reordering fucked things up
// to keep the level in its old style i am
// making "i" global until i find a fix
// -morla
int i;
//return address: 0x080484a7
//we can only overwrite 1 byte the blah address
//10th element on the stack is the return address
//10th and 8th element on the stack are our inputs(remember it's *blah and argc)
//address of our input 0xffffd7b3 and 0xffffd7b3 because blah points to b
// to print value of a variable: p *(char**)($ebp - 4) 

void func(char *b){ //*b is pointer to the address of our input 
	char *blah=b;   //*blah is a pointer pointing to the first value of b which is our input to copy from: 
					//it also contains the address of b so that's why we see b address 2 times on stakc  
	char bok[20];  
	//int i=0;
	
	memset(bok, '\0', sizeof(bok));  
	for(i=0; blah[i] != '\0'; i++) //the overflow is happening here (it keeps copying until it find a null bytes)
		bok[i]=blah[i];

	printf("%s\n",bok); 
}

int main(int argc, char **argv){
	// there is no size check for our argument 
	if(argc > 1 ) //argc is: $ebp-0x4
		func(argv[1]);
	else
	printf("%s argument\n", argv[0]);

	return 0;
}

//hey sem so i noticed after setting a break on print that the 21 value will overwrite 
// let's say i have this stack: 
0xffffd58c:	0x08048550	0xffffd594	0x41414141	0x41414141
0xffffd59c:	0x41414141	0x41414141	0x41414141	0xffffd7b7
0xffffd5ac:	0xffffd5b8	0x080484a7	0xffffd7b7	0x00000000
// 0xffffd7b7 is blah pointing to our argument 
// 0x080484a7 is EIP 
// 0xffffd7b7 is our argument 

//the byte after the 20 will overwrite that 0xffffd7b7 and will become 0xffffd742 (it will only overwrite onebyte)
//i was trying to solve like a stack canary : (20 * A) + p32(0xffffd7b7) + p32(0xffffd5b8) + bytes to overwrite EIP
//but it's not working and the address always change but now i managed to get $(python -c 'print "A" * 20 + "\xb3\xd7\xff\xff"')
//but any byte after that will make a segfault in the loop 