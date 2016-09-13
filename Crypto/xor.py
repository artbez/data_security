
f = open("encryptedtext", 'r')

g = open('text', 'w')
bb = bytearray()
for line in f:
    bb.extend(map(ord,line))
atr2 ="qwertyuiopasdfghjklzxcvbnm_"

ll = []
for i in range(0,24):
    ll.append([])
    
for i in range(0, len(bb)):
    ll[i % 24].append(bb[i])

    
d2 = []
for i in range(0,24):
    d2.append({})
    for ch in ll[i]:
        if (d2[i].get(ch) != None):
            d2[i].update({ch : d2[i][ch] + 1})
        else:
            d2[i].update({ch : 1})

for i in range(0,24):
    d2[i] = sorted(d2[i].items(), key=lambda x: x[1], reverse=True)

a = []
for i in range(0, 24):
    a.append (d2[i][0][0] ^ ord('_'))

a[11] = (a[11] ^ ord('_')) ^ ord('t')
a[20] = (a[20] ^ ord('_')) ^ ord('e')
a[5] = (a[5] ^ ord('_')) ^ ord('n')


for ch in range(0,128):
    print (ch)
    print (chr((ord('c') ^ ord('_')) ^ (ch)))
    print ()

for i in range(0, len(bb) - 24, 24):
    for j in range(0, 24):
        g.write(chr(bb[i + j] ^ a[j]))
        
for j in range(0, 24):
    print(chr(a[j]), end="")
g.write(str(a))
f.close()
g.close()
