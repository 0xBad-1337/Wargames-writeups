# level 17

## analysis:

the vulnerability here is **strcasecmp** ( yeah i also was tricked with the timing-attack stuff :( )

## vulnerability:

referring to this doc https://book.hacktricks.xyz/pentesting/pentesting-web/php-tricks-esp we can deduce that our website is vulnerable to array injection

## exploitation:

we can use directly from curl: ```curl -F "flag[]=" http://websec.fr/level17/index.php```