def remove_duplicates(value):
    value=str(value)
    temp=""
    for i in value:
        if(i in temp):
            continue
        else:
            temp=temp+i
    return temp
        

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
