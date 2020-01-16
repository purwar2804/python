def bracket_pattern(input_str):
    count1=count2=0
    if(input_str[0]=='(' and input_str[-1]==')'):
        for i in input_str:
            if(i=='('):
                count1=count1+1
            elif(i==')'):
                count2=count2+1
        if(count1==count2):
            return True
        else:
            return False
    else:
        return False

    
input_str="(())("
print(bracket_pattern(input_str))
