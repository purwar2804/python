
def check_perfect_number(number):
    k=1
    sum=0
    if(number==0):
        return 0
    while(k<number):
        if(number%k==0):
            sum=sum+k
        k=k+1
    if(sum==number):
        return 1
    else:
        return 0
def check_perfectno_from_list(no_list):
    l=[]
    for i in no_list:
        x=check_perfect_number(i)
        if(x==1):
            l.append(i)
    return l
perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)
