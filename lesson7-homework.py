'''
import random 

def words_game(words):
	for word in words:
		user_answer = ''
		while user_answer != word:
			rand_letters = ''.join(random.sample(word, len(word)))
			user_answer = input('[' + rand_letters + '] - jakie to słowo? ')
			if user_answer != word:
				print('No')
		print('Yes')
	print('You win')

list_with_words = ['python', 'dzik', 'piwo', 'tlen']
words_game(list_with_words)
'''
'''
import random
list_with_words = ['python', 'dzik', 'piwo', 'tlen']

for word in  list_with_words:
	user_answer = ''
	while user_answer != word:
		rend_word = ''.join(random.sample(word, len(word)))
		user_answer = input('Jakie to słowo?: ' + rend_word + ': ')
		if user_answer != word:
			print('No')
	print('Yes')
'''
import random

def mieszanka(slowo_do_zmieszania):
	mieszanka_list = []
	for litera in slowo_do_zmieszania:
		mieszanka_list.append(litera)
		random.shuffle(mieszanka_list)
		mieszanka_str = ''
		for el in mieszanka_list:
			mieszanka_str += el
	return mieszanka_str

list_with_words = ['piwo', 'wódka', 'ganja', 'piątek']
user_answer = ''
for word in list_with_words:
	while user_answer != word:
		user_q = mieszanka(word)
		user_answer = input('Jakie to słowo: [{}]? '.format(user_q))
		if user_answer != word:
			print ('Nie')
	print('Tak')
print('You win!')

