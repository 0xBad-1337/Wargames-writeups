#please make a bandit list I'm a lazy dude :(
#don't laugh please 
import os
import re
lvl = str(raw_input('level: '))

bandit_passwords = ["bandit0","boJ9jbbUNNfktd78OOpsqOltutMc3MY1",
					"CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9",
					"UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK",
					"pIwrPrtPN36QITSp3EQaw936yaFoFgAB",
					"koReBOKuIDDepwhWk7jZC0RTdopnAYKh",
					"DXjZPULLxYr17uwoI01bNLQbtFemEgo7",
					"HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs",
					"cvX2JJa4CFALtqS87jk27qwqGhBM9plV",
					"UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR",
					"truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk",
					"IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR",
					"5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu",
					"8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL",
					"level with ssh keys",
					"BfMYroe26WYalil77FoDi9qh59eK5xNr",
					"cluFn7wTiGryunymYOu4RcffSxQluehd",
					"bandit 17 is over private keys",
					"kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd",
					"IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x",
					"GbKksEFF4yrVs6il55v6gwY5aVje5f0j",
					"GbKksEFF4yrVs6il55v6gwY5aVje5f0j",
					"Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI",
					"jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n",
					"UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ",
					"uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG",
					"5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z",
					"3ba3118a22e93127a4ed485be72ef5ea",
					"0ef186ac70e04ea33b4c1853d2526fa2",
					"bbc96594b4e001778eee9975372716b2",
					"5b90576bedb2cc04c86a9e924ce42faf",
					"47e603bb428404d265f59c42920d81e5",
					"56a9bf19c63d650ce78e6ec0354ee45e",
					"c9c3199ddf4121b10cf581a98d51caee",]

krypton_passwords = ["nopassword","KRYPTONISGREAT","ROTTEN","CAESARISEASY","BRUTE",""]
leviathan_passwords = ["leviathan0","rioGegei8m","ougahZi8Ta","Ahdiemoo1j","vuH0coox6m","Tith4cokei","UgaoFee4li","ahy7MaeBo9"]
narnia_passwords = ["narnia0","efeidiedae","nairiepecu","vaequeezee","thaenohtai","faimahchiy","neezocaeng","ahkiaziphu","mohthuphog","eiL5fealae"]
behemoth_passwords = ["behemoth0","aesebootiv", "eimahquuof","nieteidiel","ietheishei", "aizeeshing","mayiroeche","baquoxuafo","pheewij7Ae"]

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
	os.system('ssh '+lvl+'@behemoth.labs.overthewire.org -p 2221')
if 'krypton' in lvl:
	index = re.search('[0-9]+', lvl).group()
	index = int(index)
	user_password = krypton_passwords[index] 
	print "use this password: " + user_password
	os.system('ssh '+lvl+'@krypton.labs.overthewire.org -p 2231')	
	

