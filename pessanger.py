import random
def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    
    for i in range(0,no_of_passengers):
        a=int(random.uniform(101,119))
        s=[airline+":"+source[0:3]+":"+destination[0:3]+":"+str(a)]
        ticket_number_list.append(s)
    if(len(ticket_number_list)<=5):
        return ticket_number_list
    else:
        return ticket_number_list[-5:]


print(generate_ticket("AI","Bangalore","London",7))
