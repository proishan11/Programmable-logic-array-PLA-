from tabulation import tabulation as tb 
from tabulation import printImplicants as printImplicants

def toBinary(i,no_of_variables):
	temp = ""
	for j in range(no_of_variables):
            if(i%2 == 0):
                temp = "0"+temp
            else:
                temp = "1"+temp
            i = i//2
	return temp

def main():
	print("Enter the number of variables")
	no_of_variables = int(input())
	possible_set_of_minterm = [int(x) for x in range(2**no_of_variables)]
	print(possible_set_of_minterm)
	print("Enter the number of functions")
	no_of_functions = int(input())
	
	minterms_decimal = []
	complement_minterms_decimal = []
	finalImplicants = []
	complement_finalImplicants = []
	
	for i in range(no_of_functions):
		print("Enter minterms of function {0}".format(i+1))
		temp = [int(x) for x in input().split()]
		minterms_decimal.append(temp)
	temp = []
	
	for j in minterms_decimal:
		for i in possible_set_of_minterm:
			if i not in j:
				temp.append(i)
		complement_minterms_decimal.append(temp)
		temp = []

	print(complement_minterms_decimal)
	#result = tb(no_of_variables, len(complement_minterms_decimal[0]), complement_minterms_decimal[0])
	#print(result)
	for i in minterms_decimal:
		finalImplicants.append(tb(no_of_variables, len(i), i))
	for i in complement_minterms_decimal:
		complement_finalImplicants.append(tb(no_of_variables, len(i), i))
	print(finalImplicants)
	print(complement_finalImplicants)
	set_list = []
	result = []
	
	len_result = 99999
	for i in range(2**no_of_functions):
		binary_str = toBinary(i,no_of_functions)
		temp = []
		for j in range(no_of_functions):
			if(binary_str[j] == '0'):
				temp.extend(tb(no_of_variables,len(complement_minterms_decimal[j]), complement_minterms_decimal[j]))
			else:
				temp.extend(tb(no_of_variables,len(minterms_decimal[j]),minterms_decimal[j]))
		set_temp = list(set(temp))
		set_list.append(set_temp)
		temp_len = len(set_temp)
		len_result = min(len_result,temp_len)
		
		#print(set_temp)
			#print("temp = {0}".format(temp))

	print(set_list)
	print(len_result)
	

if __name__ == '__main__':
	main()