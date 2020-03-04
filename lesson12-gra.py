from random import randint

def losowe_liczby():
	rand_str = ''
	while len(rand_str) < 4:
		i = str(randint(1, 8))
		if i not in rand_str:
			rand_str += i
		
	return rand_str

def user_numbers():
	user_str = ''
	while len(user_str) < 4:
		user_liczba = input('Wpisz niepowtarzajacą się liczbę od 1 do 8: ')
		if user_liczba not in user_str and user_liczba.isnumeric() and int(user_liczba) < 9:
			user_str += user_liczba
		else:
			print('Chuj, wpisz inną liczbę')
			
	#print(user_str)
	return user_str

def count_blacks_n_whites(user_choice, computer_choice):
	whites = 0
	blacks = 0

	for el in user_choice:
		if el in computer_choice:
			if user_choice.index(el) == computer_choice.index(el):
				blacks += 1
			else:
				whites += 1
	#print(user_choice)
	#print(computer_choice)
#	print(str(blacks) + ' ' + str(whites))
	return [blacks, whites]

def number_colors(str):
	CEND      = '\33[0m'
	CBOLD     = '\33[1m'
	CITALIC   = '\33[3m'
	CURL      = '\33[4m'
	CBLINK    = '\33[5m'
	CBLINK2   = '\33[6m'
	CSELECTED = '\33[7m'

	CBLACK  = '\33[30m'
	CRED    = '\33[31m'
	CGREEN  = '\33[32m'
	CYELLOW = '\33[33m'
	CBLUE   = '\33[34m'
	CVIOLET = '\33[35m'
	CBEIGE  = '\33[36m'
	CWHITE  = '\33[37m'

	CBLACKBG  = '\33[40m'
	CREDBG    = '\33[41m'
	CGREENBG  = '\33[42m'
	CYELLOWBG = '\33[43m'
	CBLUEBG   = '\33[44m'
	CVIOLETBG = '\33[45m'
	CBEIGEBG  = '\33[46m'
	CWHITEBG  = '\33[47m'

	CGREY    = '\33[90m'
	CRED2    = '\33[91m'
	CGREEN2  = '\33[92m'
	CYELLOW2 = '\33[93m'
	CBLUE2   = '\33[94m'
	CVIOLET2 = '\33[95m'
	CBEIGE2  = '\33[96m'
	CWHITE2  = '\33[97m'

	CGREYBG    = '\33[100m'
	CREDBG2    = '\33[101m'
	CGREENBG2  = '\33[102m'
	CYELLOWBG2 = '\33[103m'
	CBLUEBG2   = '\33[104m'
	CVIOLETBG2 = '\33[105m'
	CBEIGEBG2  = '\33[106m'
	CWHITEBG2  = '\33[107m'

	colored_str = ''

	for num in str:
		if num == '1':
			colored_str += CRED2 + num + CEND
		elif num == '2':
			colored_str += CBLUE + num + CEND
		elif num == '3':
			colored_str += CGREEN2 + num + CEND
		elif num == '4':
			colored_str += CVIOLET2 + num + CEND
		elif num == '5':
			colored_str += CBEIGE2 + num + CEND
		elif num == '6':
			colored_str += CBEIGE2 + num + CEND
		
		else:
			colored_str += num 
	#print(colored_str)
	return colored_str



won = False
comp = losowe_liczby()
i = 0

while not won:
	user_liczby = user_numbers()
	white_n_black = count_blacks_n_whites(user_liczby, comp)
	print('Liczba kompa: ' + number_colors(comp))
	if white_n_black[0] == 4:
		print('you won')
		won = True
	elif i == 3: # 4 razy
		print("Game over")
		won = True
	else:
		print('Twoja liczba: {}'.format(number_colors(user_liczby)))
		print('\33[107m' + '\33[30m' + 'You have {} blacks and {} whites points'.format(white_n_black[0], white_n_black[1]) + '\33[0m')
		i += 1

#number_colors('121323434345')
#print(losowe_liczby())
#user_numbers()
#count_blacks_n_whites(losowe_liczby(), '4567')
#print(count_blacks_n_whites(user_numbers(), losowe_liczby()))
	