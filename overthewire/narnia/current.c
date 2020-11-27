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
//address of our input 0xffffd76f adn 0xffffd7a7
// to print value of a variable p *(char**)($ebp - 4) 
void func(char *b){ //*b is pointer to the address of our input 
	char *blah=b;   //*blah is a pointer pointing to the first value of b which is our input to copy from 
	char bok[20];   //we can overflow the bok variable ebp+0x8
	//int i=0;
	
	memset(bok, '\0', sizeof(bok));
	for(i=0; blah[i] != '\0'; i++)
		bok[i]=blah[i];

	printf("%s\n",bok); // address of bok = 0xffffd5a4
}

int main(int argc, char **argv){
	// there is no size check for our argument 
	if(argc > 1)
		func(argv[1]);
	else
	printf("%s argument\n", argv[0]);

	return 0;
}

// so i tried this run $(python -c 'print 20 * "A" + "\xb3\xd7\xff\xff" + "\xb8\xd5\xff\xff" + "BBBB"')
// why? because when u check the stack after a brek on printf u notice that only 1 byte will get overwritten with the chars after 41
// show image 
// i was thinking that if i retype the correct addresses the BBBB will reach the return address and cause a segfault but that didn't happen
// weird thing that after a break point on ret i see 41414141 on top of the stack and not the return address
// so why it didn't cause a segfault 