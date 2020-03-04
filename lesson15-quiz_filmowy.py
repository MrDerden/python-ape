import requests
import json

response = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=ad9eb5c50eb3e409d9efbb6975298bc7&page=1')

print(response.status_code)
full_list = response.json().get('results')
#print(full_list)

def film_list_maker(data_from_api):
	film_dict = {}
	list_of_film_dicts = []
	for el in data_from_api:
		film_dict['id'] = el['id']
		film_dict['title'] = el['title']
		response_credits  = requests.get('https://api.themoviedb.org/3/movie/{}/credits?api_key=ad9eb5c50eb3e409d9efbb6975298bc7&page=1'.format(film_dict['id']))
		credits_cast = response_credits.json().get('crew')
		for cast_data in credits_cast:
			if cast_data["job"] == 'Director':
				director_name = cast_data['name']
				film_dict['director'] = director_name
		#print(film_dict)
		list_of_film_dicts.append(dict(film_dict))	
	return list_of_film_dicts

#film_list_maker(full_list)
file_with_film_list = open('film_list', 'w')
data_to_write = json.dumps(film_list_maker(full_list))
file_with_film_list.write(data_to_write)
file_with_film_list.close()

if file_with_film_list:
	print('Done!')

file_with_film_list = open('film_list', 'r')
content = file_with_film_list.read()
nice_content = json.loads(content)

def list_of_film_names(content_from_file):
	list_of_films = []
	for dict_with_film_info in content_from_file:
		list_of_films.append(dict_with_film_info["title"])
	return list_of_films

dostepne_filmy = list_of_film_names(nice_content)
print('Popularne filmy:')
for film in dostepne_filmy:
	print(film)
user_film = input('-----------\nWpisz film z listy zeby uzyskac info o nim: ')
if user_film in dostepne_filmy:
	for film_dict in nice_content:
		if film_dict["title"] == user_film:
			print('Reżyser filma {} - {}'.format(user_film, film_dict["director"]))
