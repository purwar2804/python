#PF-Exer-26

def factorial(number):
    fact=1
    while(number!=0):
        fact=fact*number
        number=number-1
    return fact
    
def find_strong_numbers(num_list):
    l=[]
    for i in num_list:
        num=i
        sum=0
        if(num==0):
            sum=1
        while(num!=0):
            a=num%10
            sum=sum+factorial(a)
            num=int(num/10)
        if(sum==i):
            l.append(sum)
    return l
        
   
            
            
        

num_list=[145,375,100,2,10,0]    
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
