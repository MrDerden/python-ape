# b784f35ede2a4df1a5c2fb072cfb57da

#kurs walut

import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

parameters = {
    "lat": 40.71,
    "lon": -74
}

resp = requests.get('http://api.open-notify.org/iss-pass.json', params=parameters)
#soup = BeautifulSoup(resp.content, 'xml')
#soup.find('CharCode', text='USD').find_next_sibling('Mid').string
print(resp.status_code)
print(resp.json())

def jprint(obj):
	text = json.dumps(obj, sort_keys=True, indent=4)
	print(text)

jprint(resp.json())

passtime = resp.json()['response']
jprint(passtime)

risetime = []

for d in passtime:
	risetime.append(d['risetime'])

print(risetime)

date_time = []

for smth in risetime:
	time = datetime.fromtimestamp(smth)
	date_time.append(time)
	print(time)
