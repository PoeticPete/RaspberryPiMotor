import pyrebase

config = {
	"apiKey": "AIzaSyC3tcDJPD4nXPslkhZ7gscE8p9Im4Gw00s",
	"authDomain": "easy-lock.firebaseapp.com",
  	"databaseURL": "https://easy-lock.firebaseio.com/",
  	"storageBucket": "easy-lock.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
storage = firebase.storage()

print("success!")
