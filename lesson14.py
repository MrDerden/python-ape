import os

file_name = input('Podaj nazwę pliku: ')


file = open(file_name, 'r')
my_titles = file.read()
#print(my_titles)
#titles_to_json = json.loads(my_titles)
#print(titles_to_json)

def corrector(bad_text):
	title_list = ''
	correct_dict = {
		'³': 'ł',
		'¿': 'ż',
		'¹': 'ą',
		'æ': 'ć',
		'œ': 'ś',
		'ê': 'ę',
		'¯': 'Ż'
	}

# 	countr = 0
# 	for bad, good in correct_dict.items():
# 		countr += bad_text.count(bad)
# 		bad_text = bad_text.replace(bad, good)
# 	return bad_text, countr

# correct_text, how_many_letters_were_corrected = power_corrector('Coś co podmieniamy')

	i = 0
	for el in bad_text:
		if el in correct_dict:
			el = correct_dict[el]
			title_list += el
			i += 1
		else:
			title_list += el
	print('Podmieniono ' + str(i) + ' znaków')
	return title_list

file2 = open('2', 'w')
new_titles = corrector(my_titles)
file2.write(new_titles)
file.close()
file2.close()
print('fuck yeah!!')

