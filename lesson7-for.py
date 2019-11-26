 #todo list
print('Jeśli chcesz dodać rzecz do listy, naciśnij [D]')
print('Jeśli chcesz usunąć rzecz z listy, naciśnij [U]')
print('Jesli chcesz wydrukowac liste ToDo, naciśnij [P]')
print('Żeby wyczyścić listę wpisz [C]')
print('Jeśli chcesz wyjść, naciśnij [Q]')


todo = []
user_q = ''

while user_q != 'q':
	user_q = input('Co chcesz zrobić? [D][U][P][C][Q]: ')
	user_q = user_q.lower()

	if user_q == 'd':
		todo_add = input('Wpisz rzecz, którą chcesz dodać do listy ToDo\n')
		pos_q = input('Czy chcesz dodać rzecz na konkretną pozycje? [T/N] ')
		if pos_q.lower() == 't':
			pos_n = int(input('Wpisz liczbą nr. pozycji: '))
			todo.insert((pos_n - 1), todo_add)
			print('[' + todo_add + '] - jest dodane do listy ToDo na pozycje [' + str(pos_n) + ']')
			print(todo)
		else:
			todo.append(todo_add)
			print('[' + todo_add + '] - jest dodane do listy ToDo')
			print(todo)

	elif user_q == 'u':
		pos_q = input('Czy chcesz usunąć konkretną pozycje z listy? [T/N] ')
		if pos_q.lower() == 't':
			pos_n = int(input('Wpisz liczbą nr. pozycji do usunięcia: '))
			if (pos_n-1) > len(todo):
				print('Pozycji [' + str(pos_n) + '] nie istnieje')
				print(todo)
			else: 
				todo.pop((pos_n - 1))
				print('Pozycja [' + str(pos_n) + '] została usunięta z listy ToDo')
				print(todo)
		else:
			todo_del = input('Co chcesz usunąć?\n')
			if todo_del in todo:
				todo.remove(todo_del)
				print('[' + todo_del + '] - jest usunięte z listy')
				print(todo)
			else:
				print('BLĄD! Wpisu [' + todo_del + '] nie ma na liscie ToDo')
				print(todo)

	elif user_q == 'p':
		if len(todo) > 0:
			print('Lista ToDo:')
			for todo_item in todo:
				print(todo_item)
		else:
			print('Lista ToDo jest pusta')

	elif user_q == 'c':
		todo.clear()
		print('Lista ToDo została wyczyszczona')
		print(todo)

print(todo)