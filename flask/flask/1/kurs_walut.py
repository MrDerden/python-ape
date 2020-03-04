# KURS WALUT
# Napisz aplikację we flasku, która pokaże kurs dolara amerykańskigo, funta i euro na dziś.
# Możesz wykorzystać kod z zajęć nr 11 (pobiernaie danych z serweru NBP)

# SIMPLE SERVER

# importujemy Flask
import requests
import json
from flask import Flask, render_template

# niezbędne do działania aplikacji
app = Flask(__name__)

# definijemy funkcję, która będzie odpowiedzialna za stronę
# używamy dekoratora, czyli funkcji w funkcji, podajemy URI strony
@app.route("/")
# nazwa funckji dowolna
def kurs_walut():
	response = requests.get('http://api.nbp.pl/api/exchangerates/tables/C/')
	json_list = response.json()
	rates_list = json_list[0]['rates']
	#drukujemy zformatowaną listę walut
	our_currencies = {}
	for currency_dict in rates_list:
		our_currencies[currency_dict['code']] = currency_dict['ask']
	usd_eur_gbp = "USD: {} \n EUR: {} \n GBP: {}".format(our_currencies['USD'], our_currencies['EUR'], our_currencies['GBP'])		
	return render_template('currencies.html', usd_eur_gbp = usd_eur_gbp)


# niezbędne do działania aplikacji
if __name__ == "__main__":
	app.run()

# żeby odpalić server bądź w folderze z tym plikiem i wpisz 'python server.py'