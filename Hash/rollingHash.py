flag = "Good Luck"
def RabinKarpRollingHash(string, a):
    result = 0
    l = len(string)
    for i in range(l):
        result += ord(string[i]) * (a ** (l - i - 1))
    print (result)

out = 1317748575983887541099 
RabinKarpRollingHash(flag, 256)
print (out)
