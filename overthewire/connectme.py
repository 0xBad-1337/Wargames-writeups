#please make a bandit list I'm a lazy dude :(
#don't laugh please 
import os
import re
lvl = str(raw_input('level: '))
narnia_passwords = ["narnia0","efeidiedae","nairiepecu","vaequeezee","thaenohtai","faimahchiy","neezocaeng","ahkiaziphu","mohthuphog"]
<<<<<<< HEAD
behemoth_passwords = ["behemoth0","aesebootiv"]
=======
>>>>>>> 84c96170de7f2c9d1cf4a8f56ed41b53f059b819
if 'narnia' in lvl:
	index = re.search('[0-9]+', lvl).group()
	index = int(index)
	user_password = narnia_passwords[index] 
	print "use this password: " + user_password
	os.system('ssh '+lvl+'@narnia.labs.overthewire.org -p 2226')
if 'bandit' in lvl:
	index = re.search('[0-9]+', lvl).group()
	index = int(index)
	user_password = bandit_passwords[index] 
	print "use this password: " + user_password 
	os.system('ssh '+lvl+'@bandit.labs.overthewire.org -p 2220')
if 'leviathan' in lvl:
	index = re.search('[0-9]+', lvl).group()
	index = int(index)
	user_password = leviathan_passwords[index] 
	print "use this password: " + user_password
	os.system('ssh '+lvl+'@leviathan.labs.overthewire.org -p 2223')
if 'behemoth' in lvl:
	index = re.search('[0-9]+', lvl).group()
	index = int(index)
	user_password = behemoth_passwords[index] 
	print "use this password: " + user_password
<<<<<<< HEAD
	os.system('ssh '+lvl+'@behemoth.labs.overthewire.org -p 2221')
=======
	os.system('ssh '+lvl+'@behemoth.labs.overthewire.org -p 2221')
>>>>>>> 84c96170de7f2c9d1cf4a8f56ed41b53f059b819
