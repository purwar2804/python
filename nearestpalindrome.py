def nearest_palindrome(number):
    while(1):
        number=number+1
        temp=str(number)
        rev=""
        for i in temp:
            rev=i+rev
        if(temp==rev):
            return number
        
number=12300
print(nearest_palindrome(number))
