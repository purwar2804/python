#PF-Assgn-33

def find_common_characters(msg1,msg2):
    s1=""
    for i in range(0,len(msg1)):
        for j in range(0,len(msg2)):
            if(msg1[i]!=" "):
                if(msg1[i]==msg2[j]):
                    s1=s1+msg1[i]
                    break
            else:
                break
    if(len(s1)>0):
        return s1
    else:
        return -1
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
