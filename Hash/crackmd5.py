import hashlib

myStr = "BE1DF386397C0288AAD3B435B51404EE"
myStr = myStr.lower()
f = open('passwords.txt', 'r')
for line in f:
    hash_object = hashlib.md5(line.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    if (myStr == str(hex_dig)):
        print(str(hex_dig) + " " + line)

f.close()
