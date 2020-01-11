#PF-Assgn-30

def encode(message):
    s1=""
    count=1
    for i in range(0,len(message)-1):
        if(message[i]==message[i+1]):
            count=count+1
        else:
            s1=s1+str(count)+message[i]
            count=1
    if(message[len(message)-1]!=message[len(message)-2]):
        s1=s1+"1"+message[len(message)-1]
    if(len(message)==1):
        s1="1"+message[0]
    return s1
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
