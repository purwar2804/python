def freq(string,sub):
    count=0
    m=len(string)
    n=len(sub)
    for i in range(0,m):
        if(string[i:i+n]==sub):
            count=count+1
    return count
string=input()
sub=input()
c=freq(string,sub)
print(c)
