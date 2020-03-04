from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route('/register', methods = ['POST', 'GET'])
def register():
	filename = 'usrs.txt'
			
	if request.method == 'GET':
		# stowrz HTML który zbierze login i hasło dwa razy (jak to zwykle w necie bywa)
		return render_template("create.html")
	elif request.method == 'POST':
		# sprawdź czy oba hasła się zgadzają, jeśli nie, wyświetl komuniakt
		# otwórz bazę z pliku, sprawdź czy mamy już takiego użytkownika
		# jeśli mamy, wyświetl o tym komunikat
		# jeśli nie mamy, zapisz dane tego, zamknij bazę
		result = request.form
		login = result.get('login')
		password1 = result.get('pass1')
		password2 = result.get('pass2')

		if pass_equuality(password1, password2):
			
			users_database = open(filename) #sprawdzamy czy plik nie jest pusty
			users_database.close()
			if users_database == '': #if empty
				users = {}  
				data = user_reg(login, password1, filename, users)
				
			else: # if not empty
				users_file = open(filename)
				users = json.load(users_file)
				users_file.close()
				if login in users: # przekirowanie if exist
					
					data = "Taki użytkownik juz istnieje. Sprobuj zalogować się"
				else:
					
					data = user_reg(login, password1, filename, users)
					
		else:
			
			data = "Hasła się nie zgadzają"
		
		return render_template("created_or_not.html", data=data)

@app.route('/login', methods = ['POST', 'GET'])

def logging():
	# oczywiście skorzystaj z tego co zrobiłeś/aś w poprzednim pliku
	filename = 'usrs.txt'
	
	
	if request.method == 'GET':
		# formuarz do logowania
		return render_template("logging2.html")
	elif request.method == 'POST':	
		# pobierz dane z formularza i sprawdz, czy mamy takigo użytkownika w naszej bazie z pliku
		result = request.form
		login = result.get('login')
		password = result.get('pass')

		try:
			with open(filename) as f_obj:
				users = json.load(f_obj)
		except FileNotFoundError:
			users = {}
			users[login] = password
			with open(filename, 'w') as f_obj:
				json.dump(users, f_obj)
			return users
		
		
		success = users.get(login, "No user") == password

		return render_template("logged2.html", success=success)

def pass_equuality(pass1, pass2):
	if pass1 == pass2:
		return True

def user_reg(login, password, file, dictionary):
	dictionary[login] = password
	users_file = open(file, 'w')
	json_db = json.dumps(dictionary)
	users_file.write(json_db)
	users_file.close()

	return "Zarejestrowałeś się, {}".format(login)

	
if __name__ == '__main__':
	app.run()