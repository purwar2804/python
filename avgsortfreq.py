#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    sum=0
    count=0
    for i in list_of_marks:
        sum=sum+i
    avg=sum/len(list_of_marks)
    for i in range(0,len(list_of_marks)):
        if(list_of_marks[i]>avg):
            count=count+1
    return count*100/len(list_of_marks)
        

def sort_marks():
    list_of_marks1=list(list_of_marks)
    for i in range(0,len(list_of_marks1)-1):
        for j in range(i+1,len(list_of_marks1)):
            if(list_of_marks1[i]>list_of_marks1[j]):
                temp=list_of_marks1[i]
                list_of_marks1[i]=list_of_marks1[j]
                list_of_marks1[j]=temp
    return list_of_marks1

def generate_frequency():
    l=[]
    
    for i in range(0,26):
        count=0
        for j in range(0,len(list_of_marks)):
            if(i==list_of_marks[j]):
                count=count+1
        l.append(count)
    return l
                
    
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
