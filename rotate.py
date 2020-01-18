
def one_rotate(input_list):
    l=[]
    
    temp=input_list[len(input_list)-1]
    for i in range(0,len(input_list)-1):
        l.insert(i+1,input_list[i])
    l.insert(0,input_list[len(input_list)-1])
    return l

def rotate_list(input_list,n):
    for i in range(0,n):
        x=one_rotate(input_list)
        input_list=x
    output_list=x
    
    return output_list

input_list= [1,2,3,4,5,6]
output_list=rotate_list(input_list,4)
print(output_list)
