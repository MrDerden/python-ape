import json

my_dairy = 'my_dairy'

to_do = ''
while to_do != 'q':
	to_do = input('co robimy?')

	if to_do == 'add':
		# 1 dopisz nowy wpis
		dictionary_entry = {
			'date': input('data wpisu: '),
			'content': input('\n')
		}
		# 1. daj mnie obecny zapis pamiętnika
		plik_z_pamietnikiem = open(my_dairy, 'r')
		# przerób jsona na listę słowników
		content = plik_z_pamietnikiem.read()
		# co ja tu w ogole robie?
		if len(content) == 0:
			dairy = []
		else:
			dairy = json.loads(content)
		# dodaj nowy słownik do listy
		dairy.append(dictionary_entry)
		# zrzuć listę słowników do jsona
		dairy_entry_ready_to_save = json.dumps(dairy)

		file = open(my_dairy, 'w')
		file.write(dairy_entry_ready_to_save)
		file.close()
	elif to_do == 'read':
		file = open(my_dairy, 'r')
		content = file.read()
		nice_content = json.loads(content)
		print(nice_content)
	else:
		print('?')





