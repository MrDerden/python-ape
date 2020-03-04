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