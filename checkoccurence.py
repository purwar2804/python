def check_occurence(string):
    c1=set('aA')
    c2=set('tT')
    c3=set('eE')
    count1=count2=0
    l=string.split()
    for word in l:
        for j in range(0,len(word)):
            if(word[j]=='m' or word[j]=='M'):
                if(word[j+1] in c1 and word[j+2] in c2):
                   count1=count1+1
            elif(word[j]=='j' or word[j]=='J'):
                if(word[j+1] in c3 and word[j+2] in c2):
                   count2=count2+1
    if(count1==count2):
        return True
    else:
        return False
string="Jet on the Mat but mat is too long"
print(check_occurence(string))
