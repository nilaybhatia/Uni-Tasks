input_string = "010, 1111, 1010, 10010, 100000, 10100, 110"
input_list = input_string.split(', ')
#print(input_list)
output_list = list(filter(lambda num: (int(num, 2)) % 5 == 0, input_list))
#The lambda function returns True if the current number in decimal form is divisible by 5
#Breakdown:
#int(num, 2) implies that current num i.e the i/p is in binary form
#Then it is checked whether the decimal number is divisible by 5
#If yes, then the filter function adds it to the filtered list 
ouput_string = "," .join(output_list)
print(ouput_string)
