"""
Napisz program, który w terminalu przyjmie dwie liczby, podzieli je przez siebie i wyświeli wynik w terminalu.
Obsłuż dwa błędy:
1. podane przez użytownika dane nie są konwertowalne na liczby
2. druga podana liczba to 0, a nie można dzielić przez 0 (błąd nazywa się ZeroDivisionError)
"""

# fuck = True
# while fuck:
# 	fuck = False
# 	try: 
# 		number_1 = int(input('Podaj liczbę: '))
# 	except ValueError:
# 		print('To nie liczba!')
# 		fuck = True

# duck = True
# while duck:
# 	duck = False
# 	try: 
# 		number_2 = int(input('Podaj drugą liczbę: '))
# 		if number_2 == 0:
# 			try: 
# 				res = number_1/number_2
# 			except ZeroDivisionError:
# 				print('Nie mozesz dzielić przez zero')
# 				duck = True
# 	except ValueError:
# 		print('Jo nie liczba!')
# 		duck = True

# res = number_1/number_2

# print(res)


"""
Napisz program 'Gniewny polonista', który przyjmuje kawałek tekstu i rzuca błędami:
VulgarError - jak jest w tekście "kurwa" albo "chuj"
OrthographicError - za błędy ortograficzne (żeby nie zajęło to wieków: interesuje go tylko słowo "góra" i "rzeka")
PunctuationError - za interpunkcję (j/w, interesuje go tylko przecinek przy "że")
Wykorzystaj pełną składnię obsługi błędu - niech Gniewny Polonista informuje Cie, że w Twojej wypowidzi
nie ma błędu oraz że skończył sprawdzać (niezależnie od wyniku)
"""


class VulgarError(Exception):
	def __init__(self, *args, **kwargs):
		super().__init__('Chuj Ci w cyce!', *args, **kwargs) 

class OrthographicError(Exception):
	def __init__(self, *args, **kwargs):
		super().__init__('Orphographic Ci w cyce!', *args, **kwargs) 

class PunctuationError(Exception):
	def __init__(self, *args, **kwargs):
		super().__init__('PunctuationError Ci w cyce!', *args, **kwargs) 

def convert_string(string):
	li = list(string.split(" "))
	return li

def vulgar_count(msg):
	msg_list = convert_string(msg)
	i = 0
	for word in msg_list:
		if word == "kurwa" or word == "chuj":
			i += 1
	return i

def dont_be_vulgar(msg):
	if "kurwa" in msg or "chuj" in msg:
		raise VulgarError


def check_orthography(msg):
	mistakes = ["gora", "gory" "reka", "żeka", "zece"]
	
	for mistake in mistakes:
		if mistake in msg:
			raise OrthographicError
		
def orthography_count(msg):
	i = 0
	mistakes = ["gora", "gory" "reka", "żeka", "zece"]
	
	for mistake in mistakes:
		if mistake in msg:
			i += 1

	return i		

def check_punctuation(msg):
	msg_list = convert_string(msg)
	for word in msg_list:
		if word == "że":
			word_index = msg_list.index("że")
			slowo_przed_ze = msg_list[int(word_index)-1]
			if slowo_przed_ze[-1] != ",":
				raise PunctuationError

def punctuation_count(msg):
	i = 0
	msg_list = convert_string(msg)
	for word in msg_list:
		if word == "że":
			word_index = msg_list.index("że")
			slowo_przed_ze = msg_list[int(word_index)-1]
			if slowo_przed_ze[-1] != ",":
				i += 1
	return i			

user_phrase = "Patrze z gory. Dupa konia plywie w zece, aż zalujesz że tego nie widzisz. No i chuj na ta dupę"

try:
	dont_be_vulgar(user_phrase)
except VulgarError:
	print("Vulgar errors: ", vulgar_count(user_phrase))
else:
	print("Vulgar errors: ", vulgar_count(user_phrase))


try:
	check_orthography(user_phrase)
except OrthographicError:
	print("Orthographic errors: ", orthography_count(user_phrase))
else:
	print("Orthographic errors: ", orthography_count(user_phrase))
	
try:
	check_punctuation(user_phrase)
except PunctuationError:
	print("Punctuation Errors: ", punctuation_count(user_phrase))
else:
	print("Punctuation Errors: ", punctuation_count(user_phrase))
	