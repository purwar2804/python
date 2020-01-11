#PF-Assgn-36
'''Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers.
Note: Assume that all the numbers are two digit numbers.'''


def create_largest_number(number_list):
    for i in range(0,len(number_list)-1):
        for j in range(i+1,len(number_list)):
            if(number_list[i]<number_list[j]):
                temp=number_list[i]
                number_list[i]=number_list[j]
                number_list[j]=temp
    print(number_list)
    s=""
    for i in number_list:
        s=s+str(i)
    return int(s)
number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
