import requests
import json

response = requests.get('http://api.nbp.pl/api/exchangerates/tables/C/')

print(response.status_code)
json_list = response.json()
#print(json_list)
#print(json.dumps(json_list, sort_keys=True, indent=2))
#our_dict = json.loads(json_dict)
#json_dict = json_list[0]
rates_list = json_list[0]['rates']
print(json.dumps(rates_list, sort_keys=True, indent=2))

#drukujemy zformatowaną listę walut
for currency_dict in rates_list:
	print('valuta: [{}] kurs kupna [{}], kurs sprzedarzy [{}]'.format(currency_dict['code'], currency_dict['bid'], currency_dict['ask']))

def find_currency(currency):
	for currency_dict in rates_list:
		if currency_dict['code'] == currency:
			ask_currency = currency_dict['ask']
	return ask_currency


waluta = (input('Którą walutę chcesz kupić? ')).upper()

currency_list = [] #tworzymy listę dostepnych w api walut

for currency_dict in rates_list:
	for k, v in currency_dict.items():
		if k == 'code':
			currency_list.append(v)
print(currency_list)

if waluta in currency_list:			
	ile = input('Ile {} chcesz kupić? '.format(waluta))
	while not ile.isnumeric():
		print('Nieprawidłowy format, wpisz liczbę')
		ile = input('Ile {} chcesz kupić? '.format(waluta))
		if ile.isnumeric():
			res = int(ile) * find_currency(waluta)
			print('Dawaj {} zł.'.format(res))
	
else:
	print('Wpisz poprawniw walutę!')