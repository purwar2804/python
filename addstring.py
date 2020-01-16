def add_string(str1):
    if(len(str1)<3):
        return str1
    else:
        if(str1[-3:len(str1)]=="ing"):
            str1=str1+"ly"
        else:
            str1=str1+"ing"
            
    return str1

str1="com"
print(add_string(str1))
