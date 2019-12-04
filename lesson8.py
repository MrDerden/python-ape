list_in = ['My', 'good', 'pepelatz']

def the_longest(the_list):
	for el in the_list:
		max_len = ''
		if len(el) > len(max_len):
			max_len = el
	return max_len

print(the_longest(list_in))