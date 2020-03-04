# b784f35ede2a4df1a5c2fb072cfb57da

#kurs walut

import requests
import json
'''
resp = requests.get('http://api.nbp.pl/api/exchangerates/tables/a/today/')

waluta = input('Kurs której waluty chcesz wiedzieć? [USD],[EUR],[CZK]: ')
waluta = waluta.upper()

#print(resp.status_code)
#print(resp.json())

def jprint(obj):
	text = json.dumps(obj, sort_keys=True, indent=4)
	#print(text)

#jprint(resp.json())

def find_currency(currency):

	for x in resp.json():
		for k, v in x.items():
			if k == 'rates':
				jprint(v) # lista slownikow walut (rates)
				for curr_dict in v:
					if curr_dict['code'] == currency:
						currency_mid_value = curr_dict['mid']
	return currency_mid_value

if waluta == 'USD' or waluta == 'EUR' or waluta == 'CZK':	
	print('Kurs {}: {}'.format(waluta, find_currency(waluta)))
else:
	print('Fuck')					
'''
#prognoza

resp = requests.get('weatherAPI')
