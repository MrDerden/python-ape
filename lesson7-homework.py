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