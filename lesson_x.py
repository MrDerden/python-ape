def symbol_counter(our_string):
	return len(our_string)

def digit_checker(our_string):
	if our_string.isdigit():
		return int(our_string)
	else:
		return 'Not a number'

def a_checker(our_string):
	our_string = our_string.lower()
	return our_string.count('a')

def find_vowels(our_string):
	our_string = our_string.lower()
	vowels = 0
	vowels += our_string.count('a')
	vowels += our_string.count('e')
	vowels += our_string.count('i')
	vowels += our_string.count('y')
	vowels += our_string.count('o')
	return vowels

the_phrase = 'Cotozachaslawogulienierazumiem'
the_number = '1212314245'
print(symbol_counter(the_phrase))
print(digit_checker(the_number))
print(a_checker(the_phrase))
print(find_vowels(the_number))

#cinema tickets
'''
age = input('Podaj swoj wiek\n')
while not (age.isdigit()):
	age = input('Podaj wiek liczbą\n')

age = int(age)
if age < 3:
	print('Wejsćie jest biezpłatne')
elif (age >= 3) and (age < 12):
	print('Wejsćie kosztuje 10$')
elif age >= 12:
	print('Wejśćie kosztuje 15$')
'''

# filmowy doradca

detektyw = ['kolombo', 'chinatown', 'puaro']
action = ['comando', 'terminator', 'rambo']
fantasy = ['lord of the rings', 'avatar', 'hobbit']

film_name = input('Wpisz nazwę filmu\n')
film_name = film_name.lower()
while film_name:
	if film_name in detektyw:
		print('Gatunek filmu ' + film_name.title() +': detktyw')
		break
	elif film_name in action:
		print('Gatunek filmu ' + film_name.title() +': film akcja')
		break
	elif film_name in fantasy:
		print('Gatunek filmu ' + film_name.title() +': fantasy')
		break
	elif not ((film_name in detektyw) and (film_name in action) and (film_name in fantasy)):
		film_name = input('Wpisz inną nazwe filmu\n')
	 
#just string to commit