#PF-Assgn-44
'''Write a python function find_duplicates(), which accepts a list of numbers and returns another list containing all the duplicate values in the input list. If there are no duplicate values, it should return an empty list.

Also write the pytest test cases to test the program.
'''
def find_duplicates(list_of_numbers):
    l=[]
    for i in range(0,len(list_of_numbers)-1):
        for j in range(i+1,len(list_of_numbers)):
            if(list_of_numbers[i]==list_of_numbers[j]):
                if(list_of_numbers[i] not in l):
                    l.append(list_of_numbers[i])
                
    return l
list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
