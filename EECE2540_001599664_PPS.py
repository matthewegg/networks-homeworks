import math # import math module in order to accurately represent pi
import csv	# import csv module in order to read lines of csv files
import re	# import re module in order to use regular expressions to detect email addresses and valid hexidecimal strings

# Author: Matthew Egg

class PacketClass:
	
	def __init__(self, packet_t):
		"""
		Constructor for PacketClass
		Initializes the PacketClass object with the given tuple
		ParityValid is initialized to -1 as default and can be changed using member functions
		:param packet_t: tuple of (packet_id, destination, source, data, parity_bit)
		"""
		self.packet_id = packet_t[0]	# packet_id initialized to first element of tuple
		self.destination = packet_t[1]	# destination initialized to second element of tuple
		self.source = packet_t[2]	# source initialized to third element of tuple
		self.data = packet_t[3]	# data initialized to fourth element of tuple
		self.parity_bit = packet_t[4] 	# parity_bit initialized to fifth element of tuple
		self.ParityValid = -1	# ParityValid initialized to -1 as default
    
	def check_parity(self, data, rcvd_parity):
		"""
		Checks the parity of the data and sets the ParityValid member variable based on whether the given parity bit was correct
		:param data: data to check parity of
		:param rcvd_parity: parity bit received
		"""
		numOnes = data.count("1")	# count the number of ones in the data
		bit = numOnes % 2	# calculate the parity bit
		if bit == int(rcvd_parity):	# check if the calculated parity bit matches the received parity bit
			self.ParityValid = True	# set ParityValid to True if the parity bits match
		else:
			self.ParityValid = False	# set ParityValid to False if the parity bits do not match
    
	def parsed_packet(self):
		"""
		Returns a string representation of the given packet
		:return: string of the form "Received Packet Number <packet_id> from node <source>. Parity Check returns <ParityValid>"
		"""
		# return the string representation of the packet
		return "Received Packet Number " + self.packet_id + " from node "  + self.source +  ". Parity Check returns " + str(self.ParityValid)

def problem_one( string_to_be_reversed ):
	"""
	Reverses the given string
	:param string_to_be_reversed: string to be reversed
	:return: reversed string
	"""
	if isinstance(string_to_be_reversed, str) and len(string_to_be_reversed) > 0:	# check if the input is a string and is not empty
		return string_to_be_reversed[::-1]	# return the reversed string
	else:
		return "None"	# return None if the input is not a string or is empty

def problem_two( number_to_find , list_to_check ):
	"""
	Checks if the given number is in the given list
	:param number_to_find: number to look for
	:param list_to_check: list to check
	:return: True if number_to_find is in list_to_check, False otherwise
	"""
	state = True	# state variable to keep track of whether the list is valid
	# check if the list is valid and contains only numbers
	if isinstance(list_to_check, list) and len(list_to_check) > 0 and isinstance(number_to_find, int) or isinstance(number_to_find, float):
		for item in list_to_check:	# check if each item in the list is a number
			if not isinstance(item, int):
				state = False

	if state == True:	# if the list is valid and contains only numbers, check if the number is in the list
		return number_to_find in list_to_check
	else:
		return "None"	# return None if the list is not valid or does not contain only numbers

def problem_three( integer_to_sum_to ):
	"""
	Sums all integers from 0 to the given integer
	:param integer_to_sum_to: integer to sum to
	:return: sum of all integers from 0 to integer_to_sum_to
	"""
	if isinstance(integer_to_sum_to, int) and integer_to_sum_to > 0:	# check if the input is a positive integer
		sum = 0	# variable to store the sum of all integers from 0 to integer_to_sum_to
		for num in range(integer_to_sum_to + 1):
			sum += num	# add each integer from 0 to integer_to_sum_to to the sum
		return sum	# return the sum
	else:
		return "None"	# return None if the input is not a positive integer

def problem_four( left_list , right_list ):
	"""
	Combines the two given lists into one list with no duplicates
	:param left_list: first list
	:param right_list: second list
	:return: list containing all elements from left_list and right_list with duplicates removed
	"""
	# check if the inputs are valid lists and not empty
	if isinstance(left_list, list) and len(left_list) > 0 and isinstance(right_list, list) and len(right_list) > 0:
		return list(set(left_list + right_list))	# return the combined list with duplicates removed
	else:
		return "None"	# return None if the inputs are not valid lists or are empty

def problem_five( radius ):
	"""
	Calculates the area of a circle with the given radius
	:param radius: radius of the circle
	:return: area of the circle
	"""
	if isinstance(radius, int) or isinstance(radius, float):	# check if the input is a number
		return math.pi * radius ** 2	# return the area of the circle
	else:
		return "None"	# return None if the input is not a number

def problem_six( filename ):
	"""
	Reads the given csv file and returns a list of lists containing the data from the csv file
	Another note: I saw that the version of the response in the assignment description had each element as an integer, but since the csv files has the potential to have words or characters in it, I chose to leave the elements as strings
	:param filename: name of the csv file to read
	:return: list of lists containing the data from the csv file
	"""
	if isinstance(filename, str) and len(filename) > 0:	# check if the input is a string and is not empty
		try:	# try to open the file
			with open(filename + '.csv', newline='') as csvfile:
				reader = csv.reader(csvfile, delimiter=',')	# read the csv file
				data = []	# list to store the data from the csv file
				for row in reader:	# add each row to the data list
					data.append(row)
				return data	# return the data list
		except:
			return "None"	# return None if the file cannot be opened
	else:
		return "None"	# return None if the input is not a string or is empty

def problem_seven( hex_string ):
	"""
	Converts the given hex string to ascii
	:param hex_string: hex string to convert
	:return: ascii string
	"""
	hex_regex = r'^[0-9a-fA-F]+$'	# regex to check if the input is a valid hex string (can only contain numbers 0-9 and letters a-f or A-F)
	if bool(re.match(hex_regex, hex_string)) and len(hex_string) % 2 == 0:	# check if the input is a valid hex string
		asciiStr = ""	# string to store the ascii string
		for i in range(0, len(hex_string), 2):	# convert each pair of hex characters to ascii and add them to the ascii string
			hexChar = hex_string[i:i+2]
			asciiChar = chr(int(hexChar, 16))
			asciiStr += asciiChar
		return asciiStr	# return the ascii string
	else:
		return "None"	# return None if the input is not a valid hex string

def problem_eight( list_of_lists ):
	"""
	Multiplies the last element of each list within the larger list by 2
	:param list_of_lists: list of lists of integers
	:return: list of lists with the last element of each list multiplied by 2
	"""
	state = True	# state variable to keep track of whether the list is valid
	if isinstance(list_of_lists, list) and len(list_of_lists) > 0:	# check if the input is a list and is not empty
		for item in list_of_lists:	# check if each item in the list is a list of integers
			if isinstance(item, list) and len(item) > 0:
				for num in item:
					if not isinstance(num, int):	# check if each element in each sub-list is an integer
						state = False
			else:
				state = False	# set state to False if the list is not a list of integers
	else:
		state = False	# set state to False if the input is not a list or is empty
	
	if state == True:	# if the list is valid, multiply the last element of each sub-list by 2
		for item in list_of_lists:
			item[-1] *= 2
		return list_of_lists	# return the updated list
	else:
		return "None"	# return None if the list is not valid
		

def problem_nine( list_of_email_addresses ):
	"""
	Extracts all unique domain names from the given list of email addresses
	:param list_of_email_addresses: list of email addresses
	:return: list of domain names
	"""
	domains = []	# list to store the domain names
	if isinstance(list_of_email_addresses, list) and len(list_of_email_addresses) > 0:	# check if the input is a list and is not empty
		email_regex = r'^[a-z0-9]+@[a-z]+\.[a-z]+$'	# regex to check if the input is a valid email address (username can contain numbers 0-9 and letters a-z, domain name and extension can contain letters a-z only)
		for email in list_of_email_addresses:	# extract the domain name from each email address and add it to the domains list
			if bool(re.match(email_regex, email)):	# check if the email address is valid based on the regex pattern
				if email.split("@")[1] not in domains:	# check if the domain name has already been added to the domains list
					domains.append(email.split("@")[1])	# it not, add the domain name to the domains list
		return domains	# return the domains list
	else:
		return "None"	# return None if the input is not a list or is empty

def problem_ten( packet_t ):
	"""
	Checks the parity of the given packet and returns a string representation of the packet
	:param packet_t: tuple of (packet_id, destination, source, data, parity_bit)
	:return: string representation of the packet
	"""
	pkt_o = PacketClass(packet_t)	# create a PacketClass object with the given packet tuple
	pkt_o.check_parity(pkt_o.data, pkt_o.parity_bit)	# check the parity of the packet
	return pkt_o.parsed_packet()	# return the string representation of the packet using the parsed_packet member function

# Program entry point.
if __name__ == '__main__':
	# call each function with the given test cases
	print(problem_one("Hello World!"))
	print(problem_two(8, [1, 2, 3, 4, 5]))
	print(problem_three(6))
	print(problem_four([1, 2, 3], [2, 3, 4]))
	print(problem_five(3))
	print(problem_six('MyData'))
	print(problem_seven('48656c6c6f20576f726c6421'))
	print(problem_eight([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
	print(problem_nine(['cats@gmail.com', 'Hello World!', 'dogs@gmail.com', 'cows@yahoo.com']))
	print(problem_ten(('2','10', '5', '01100101011000101011001001110110', '0')))