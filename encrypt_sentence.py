#PF-Assgn-47
def encrypt_sentence(sentence):
    s=""
    l=[]
    word=sentence.split()
    vowel=['a','e','i','o','u','A','E','I','O','U']
    for i in range(0,len(word)):
        b=""
        c=""
        if((i+1)%2==0):
            for j in word[i]:
                if j in vowel:
                    b=b+j
                else:
                    c=c+j
            l.append(c+b)
        else:
            rev=""
            rev=word[i][::-1]
            l.append(rev)
    for i in range(0,len(l)):
        s=s+l[i]
        if(i!=len(l)-1):
            s=s+" "
    return s

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
