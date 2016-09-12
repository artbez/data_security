import codecs

str = "ПГПГ ПЮОГ УГПЦ"

for i in range(32):
    for j in str:
        print (chr(ord(j) + i), end = "")
    print()
    
