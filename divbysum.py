
def divisible_by_sum(number):
    sum=0
    temp=number
    while(number!=0):
        sum=sum+number%10
        number=int(number/10)
    if(temp%sum==0):
        return True
    else:
        return False
    
        
    
number=42
print(divisible_by_sum(number))
