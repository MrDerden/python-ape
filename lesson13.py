#kalendarz
'''
calendar = [
	{'what': 'clean dishes', 'when': 'monday'}
]

todo = ''

while todo != 'q':
	todo = input('what would you like to do? [add]/[show day]/[q]')
	if todo == 'add':
		calendar.append({'what': input('What?'), 'when': input('When?')})

	elif todo == 'show day':
		the_day = input('What day? ')
		for d in calendar:
			if the_day == d['when']:
				print(d)

	elif todo == 'show calendar':
		print(calendar)

	elif todo == 'remove':
		to_remove = input('what to remove? ')
		for d in calendar:
			if d['what'] == to_remove


print(calendar)
'''

#zapisywanie w plik
import json

my_dairy = 'my_dairy'

todo = ''
while todo != 'q':
	todo = input('what to do?')
	if todo == 'add':
		dictionary_entry = {
			'date': input('data wpisu: '),
			'content': input('write smth: ')
		}
		#daj mi obecny dairy
		plik_pamietnika = open(my_dairy, 'r')
		#przerob jsona na liste slownikow
		content = plik_pamietnika.read()
		#dodaj dodaj nowy slownik do listy
		if len(content) == 0:
			dairy = []
		else:
			dairy = json.loads(content)
		
		dairy.append(dictionary_entry)
		#print(dairy)

		dict_ready_to_save = json.dumps(dairy)
		#print(dict_ready_to_save)
		file = open(my_dairy, 'w')
		file.write(dict_ready_to_save)
		file.close()
	elif todo == 'show':
		file = open(my_dairy, 'r')
		content = file.read()
		nice_content = json.loads(content)
		print(nice_content)
	else:
		print('whaaaaat?')