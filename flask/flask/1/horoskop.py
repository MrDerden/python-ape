# HOROSKOP
# Przygotuj stronę we flasku z horoskopem.
# Stwórz listę ogólnych i zawsze dobrych porad życiowych,
# typu "Nigdy nie jest za późno" albo "Ważne są tylko te dni których jeszcze nie znamy"
# Niech program wylosuje jedną z porad i umieści ją w templatece.
# Przy odświeżeniu strony powinna pojawić się inna porada.

# SIMPLE SERVER

# importujemy Flask
from flask import Flask
import random

# niezbędne do działania aplikacji
app = Flask(__name__)

# definijemy funkcję, która będzie odpowiedzialna za stronę
# używamy dekoratora, czyli funkcji w funkcji, podajemy URI strony
@app.route("/")
# nazwa funckji dowolna
def horo():
	lista_porad = ['Będź grzeczny', 'Lub innych ludzi', 'Nie pij piwa']
	return random.choice(lista_porad)


# niezbędne do działania aplikacji
if __name__ == "__main__":
	app.run()

# żeby odpalić server bądź w folderze z tym plikiem i wpisz 'python server.py'