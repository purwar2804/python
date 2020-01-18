
def find_gcd(num1,num2):
    l=[]
    if(num1>num2):
        for i in range(1,num2+1):
            if(num1%i==0 and num2%i==0):
                l.append(i)
    else:
        for i in range(1,num1+1):
            if(num1%i==0 and num2%i==0):
                l.append(i)
    return max(l)

num1=45
num2=9
print(find_gcd(num1,num2))
