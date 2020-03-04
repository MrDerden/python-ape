'''
renge_number = input('Wpisz liczbę')

def make_squares(liczba):
	slownik = {}
	for i in range(1, (int(liczba)+1)):
		j = i*i
		slownik[i] = j
	return slownik

print(make_squares(renge_number))
'''
#2
sl_in = {'a': 'abba', 'b':'Banaś'}
sl_out = {}

for k, v in sl_in.items():
	sl_out[v] = k
print(sl_out)

#3
str_in3 = 'Banaś słucha ABBA'

def count_el_in_string(the_string):
	the_string = the_string.lower()
	sl_out3 = {}
	for i in the_string:
		#print(i + ':' + str(str_in3.count(i)))
		sl_out3[i] = the_string.count(i)
	return sl_out3

print (str_in3)
print(count_el_in_string(str_in3))

#4

sl_in4_1 = {'a': 22, 'b': 54, 'c': 'Banaś'}
sl_in4_2 = {'a': 12, 'c': 'słucha ABBA'}
sl_out4 = {}

for i, j in sl_in4_1.items():
	for x, y in sl_in4_2.items():
		if i == x:
			wartosc = j + y
			sl_out4[i] = wartosc
print(sl_out4)

#5

sl5_in1 = {'k1':1, 'k2':3, 'k3':2}
sl5_in2 = {'k1':1, 'k2':2}
sl5_out = {}

for k, v in sl5_in1.items():
	for i, j in sl5_in2.items():
		if k == i and v == j:
			sl5_out[k] = v
print(sl5_out)

#6 Program wyszukuje unikalne klucze na postawie listy slowników
#in: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#out: ['S005', 'S002', 'S007', 'S001', 'S009']

str_of_dicts = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

	#bierzemy unikalne klucze i zwracamy ich wartosci
def uniq_keys_value(list_of_dictionaries): 
	str_of_keys = []
	str_of_uniq_dicts = []
	list_of_uniq_keys_value = []
	for dictn in list_of_dictionaries:
		for k in dictn:
			if k not in str_of_keys:
				str_of_keys.append(k)
				str_of_uniq_dicts.append(dictn)
				list_of_uniq_keys_value.append(dictn[k])
	#print(str_of_keys)
	#print(str_of_uniq_dicts)
	return list_of_uniq_keys_value

	#bierzemy unikalne klucze i zwracamy ich wartosci / sposób 2
def uniq_keys_value_2(list_of_dictionaries):
	dict_of_uniq_keys = {}
	list_of_uniq_key_values = []
	for dictn in list_of_dictionaries:
		for k, v in dictn.items():
			dict_of_uniq_keys[k] = v
			#print(dict_of_uniq_keys)
	for key in dict_of_uniq_keys:
		list_of_uniq_key_values.append(dict_of_uniq_keys[key])
	#print(dict_of_uniq_keys)
	return list_of_uniq_key_values

	#zwracamy unikalne wartości
def uniq_values(list_of_dictionaries):
	list_of_values = []
	for dictn in list_of_dictionaries:
		for v in dictn.values():
			if v not in list_of_values:
				list_of_values.append(v)
	return list_of_values

print(uniq_keys_value(str_of_dicts)) #['S001', 'S001', 'S005', 'S007']
print(uniq_keys_value_2(str_of_dicts)) #['S009', 'S005', 'S005', 'S007']
print(uniq_values(str_of_dicts)) #['S001', 'S002', 'S005', 'S009', 'S007']