def count_digits_letters(sentence):
    letterc=0
    digitc=0
    result_list=[]
    letter=set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    digit=set('0123456789')
    for i in sentence:
        if(i in letter):
            letterc=letterc+1
        elif(i in digit):
            digitc=digitc+1
    result_list.append(letterc)
    result_list.append(digitc)
    
    
    return result_list

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))
