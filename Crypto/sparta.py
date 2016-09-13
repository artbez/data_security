str1 = "GRIREAAEEALRALSNNLLITFT EWAVHPT"
for i in range(1, len(str1)):
    for k in range(0, i+1):
        for j in range(0, len(str1)):
            if (j % i == k):
                print(str1[j], end="")
        print()        
    print("\n\n\n" + str(i))
         
