def substring(s):
    for i in range(0,len(s)):
        s1=""
        for j in range(i,len(s)):
            s1=s1+s[j]
            print(s1)


s=input("input")
substring(s)
