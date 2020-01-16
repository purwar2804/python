
def calculate_net_amount(trans_list):
    sum=0
    for st in trans_list:
        word=st.split(':')
        if(word[0]=='D'):
            sum=sum+int(word[1])
        elif(word[0]=='W'):
            sum=sum-int(word[1])
    net_amount=sum
    
    return net_amount

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))
