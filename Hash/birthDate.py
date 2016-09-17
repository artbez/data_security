import hashlib

myStr = "a58dc2cfc5a93134666c607fbc5d6e961254214a"

for i in range(10000000, 99999999):
    hash_object = hashlib.sha1(str(i).encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    if (myStr == str(hex_dig)):
        print(str(hex_dig) + " " + str(i))
