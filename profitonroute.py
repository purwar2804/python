def calculate(distance,no_of_passengers):
    earn=no_of_passengers*80
    fuel=7*distance
    if(earn-fuel>0):
        return earn-fuel
    else:
        return -1


#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
