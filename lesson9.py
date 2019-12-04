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