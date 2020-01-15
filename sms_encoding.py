def sms_encoding(data):
    vowel=('a','e','i','o','u','A','E','I','O','U')
    word=data.split()
    l=[]
    for i in word:
        s=""
        for j in i:
            if( j in vowel):
                continue
            else:
                s=s+j
        if(len(s)>0):
            l.append(s)
        else:
            l.append(i)
    var=""
    for i in range(0,len(l)):
        var=var+l[i]
        if(i!=len(l)-1):
            var=var+" "
    return var
data="I love Python"
print(sms_encoding(data))
