"""Write a python function find_smallest_number() which accepts a number n and returns the smallest number having n divisors.
Handle the possible errors in the code written inside the function."""
def factor(temp):
    count=0
    for i in range(1,temp+1):
        if(temp%i==0):
            count=count+1
    return count
def find_smallest_number(num):
    temp=1
    while(1):
        x=factor(temp)
        if(x==num):
            return temp
        else:
            temp=temp+1
        
    

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
