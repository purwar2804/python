def bracket(string):
    l=[]
    for i in range(0,len(string)):
        if(string[i]=='(' or string[i]=='{' or string[i]=='['):
            l.append(i)
        else:
            if(string[i]==')' and l[len(l)-1]=='('):
                l.pop()
            elif(string[i]=='}' and l[len(l)-1]=='{'):
                l.pop()
            elif(string[i]==']' and l[len(l)-1]=='['):
                l.pop()
            else:
                p=i+1
                return p

    if(
        len(l)==0):
        return True
    else:
        p=len(l)+2
        return False

s=input()
print(bracket(s))
