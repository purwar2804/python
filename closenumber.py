import math
def close_number(num1,num2,num3):
    if(math.fabs(num1-num2)<=1):
        close=num1
    elif(math.fabs(num1-num3)<=1):
        close=num1
    elif(math.fabs(num2-num3)<=1):
        close=num3
    else:
        return False
    if(close==num1 and math.fabs(num2-num3)>=2):
        return True
    elif(close==num3 and math.fabs(num1-num2)>=2):
        return True
    else:
        return False

print(close_number(5,4,2))



