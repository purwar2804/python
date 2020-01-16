def string_both_ends(input_string):
    
	if(len(input_string)<2):
	    return -1
	else:
	    return input_string[0]+input_string[1]+input_string[-2]+input_string[-1]

input_string="w3w"
print(string_both_ends(input_string))
