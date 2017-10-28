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

def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

lock_firebase_stream = db.child("doors/door1/status").stream(stream_handler)
