#11 Write a Python function that takes two lists and returns True if they have at least one common member.

def lists_comparer (list1, list2):
	for el1 in list1:
		for el2 in list2:
			if el1 == el2:
				return True

print(lists_comparer([1, 5, ' dsdcsdcsdcs'], ['xadsxadxasxaxs', 'de', 1]))

#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

sample_list.pop(4)
sample_list.pop(3)
sample_list.pop(0)

print(sample_list)

#14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

sample_list = [7, 12, 32, 44, 32, 67, 987, 67]
clear_list =[]

for n in sample_list:
	if n%2 != 0:
		clear_list.append(n)

print(clear_list)

#15. Write a Python program to shuffle and print a specified list.

import random

sample_list = ['good', 'bad', 'ugly']
random.shuffle(sample_list)
print(sample_list)

#16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included)

def list_of_squares(i, j):
	clear_list = []
	i = i-1
	while i <= j:
		i += 1
		clear_list.append(i**2)
	return clear_list

def list_of_five(the_list):
	fiths = []
	fiths.extend(the_list[:5])
	fiths.extend(the_list[-5:])
	return fiths	

print(list_of_squares(1, 30))
print(list_of_five(list_of_squares(1, 30)))