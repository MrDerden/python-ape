moj_slownik = {
	'imie' : 'Roman',
	'rozmiar' : 43,
	'czy lubisz koty' : 'tak'
}
'''
q = input('co chcesz znac o sobie? ')
if q in moj_slownik.keys(): # or use if q is not None
	print(moj_slownik.get(q))
else:
	print('fak')
'''
'''
q = input('co chcesz znac o sobie? ')
if q == 'admin123':
		add_to_dict = input('podaj nowa wartosc ')
		moj_slownik['new_key'] = add_to_dict
elif q == 'wszystko':
	for k, v in moj_slownik.items():
		print('My {} is {}'.format(k, v))
elif q in moj_slownik.keys(): # or use if q is not None
	print(moj_slownik.get(q))
else:
	print('fak')

print(moj_slownik)
'''

# 9 - homework

print ('[1] - Dodaj ucznia')
print ('[2] - Dodaj ocene ucznia')
print ('[3] - Policz średnią ucznia')
print ('[4] - Policz średnią klasy')
print ('[5] - Wylistuj uczniów')
print ('[6] - Wylistuj uczniów i ich średnią oceną')
print ('[q] - Exit')

def dodac_ucznia(the_uczen, the_dziennik):
	the_dziennik[the_uczen] = []
	return the_dziennik

def dodac_ocene(the_uczen, the_dziennik):
	if the_uczen in the_dziennik:
		ocena = input('Dodaj ocenę do {}: '.format(the_uczen))
		the_dziennik[the_uczen].append(ocena)
	else:
		print('Nie znaleziono ucznia {}'.format(the_uczen))

def srednia_arytmietyczna_ucznia(the_uczen, the_dziennik):
	sr_ar_ucznia = 0
	sum_ucznia = 0
	for val in the_dziennik[the_uczen]:
		sum_ucznia += int(val)
		
	sr_ar_ucznia = sum_ucznia/len(the_dziennik[the_uczen])
	return sr_ar_ucznia

def srednia_arytmietyczna_klasy(the_dziennik):
	sum_klasy = 0
	ilosc_ocen_klasy = 0
	for lista_ocen in the_dziennik.values():
		ilosc_ocen_klasy += len(lista_ocen)
		for ocena_z_listy in lista_ocen:
			sum_klasy += int(ocena_z_listy)
	print('Suma ocen klasy = ' + str(sum_klasy))
	print('ilość ocen : ' + str(ilosc_ocen_klasy))
	sr_ar_klasy = sum_klasy/ilosc_ocen_klasy
	return sr_ar_klasy

dziennik = {
	'kolia' : ['5', '4', '4'],
	'vasia' : ['3', '3', '3']
}
user_q = ''
while user_q != 'q':
	user_q = input('Cochcesz zrobić?: ')
	if user_q == '1':
		new_uczen = input('Wpisz imie ucznia: ')
		dodac_ucznia(new_uczen, dziennik)
		print(dziennik)
	elif user_q == '2':
		print(dziennik)
		uczen = input('Wpisz imie uczna, któremu chcesz dodać ocenę: ')
		dodac_ocene(uczen, dziennik)
		print(dziennik)
	elif user_q == '3':
		print(dziennik)
		uczen = input('Wpisz imie ucznia, dla którego chcesz policzyć średnią ocenę: ')
		print('Średnia ocena ucznia [{}] to [{}]'.format(uczen, srednia_arytmietyczna_ucznia(uczen, dziennik)))
	elif user_q == '4':
		print(dziennik)
		print('Średnia arytmietyzna klasy = {}'.format(srednia_arytmietyczna_klasy(dziennik)))
	elif user_q == '5':
		for uczen_name in dziennik.keys():
			print(uczen_name)
	elif user_q == '6':
		for uczen_name in dziennik.keys():
			print('{} ma średnią ocenę {}'.format(uczen_name.title(), srednia_arytmietyczna_ucznia(uczen_name, dziennik)))
	elif user_q != 'q':
		print('I`m sorry, I`m a table')