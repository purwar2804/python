def diagonal_stars(number):
    for i in range(0,number):
        t=i
        while(t):
            print(".",end="")
            t=t-1
        print("*")
        

number=6    
diagonal_stars(number)
