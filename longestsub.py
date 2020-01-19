def longest_substring(string):
    l=[]
    for i in range(0,len(string)):
        s1=string[0]
        for j in range(i+1,len(string)):
            if(string[j] not in s1):
                s1=s1+string[j]
            else:
                if(len(s1)>=3):
                    l.append(s1)
    s2=""
    for k in l:
        if(len(k)>len(s2)):
            s2=k
    return s2

string=input()
print(longest_substring(string))
        
