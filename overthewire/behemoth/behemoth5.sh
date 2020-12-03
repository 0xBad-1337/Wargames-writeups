#with gdb we can see a lot of system call we've never seen before
#we notice socket and atoi() which means the program is sending some data to a port
#push   0x80489e4 before atoi is pushing 1337 to get converted to int we can assume that 1337 is the port
#x/s 0x80489c5 before gethostbyname@plt is pushing  localhost to function
#push   0x0 push   0x2 push   0x2: notice those value are pushed to stack before socket@plt
#0 stands for IP
#2 stands for UDP
#2 stands for AF_INET(IPv4)
# to solve this we just need to setup a nc on port 1337 for UDP protocol

nc -ulp 1337
