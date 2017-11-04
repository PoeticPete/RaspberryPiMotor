import RPi.GPIO as gpio		# Used to connect to Raspberry Pi
import time					# Used to sleep main thread for lock
import pyrebase				# Used to connect to Firebase


def init():
	'''
	Setup Raspberry Pi GPIO pins.

	'''
	gpio.setmode(gpio.BCM)
	gpio.setup(17, gpio.OUT)
	gpio.setup(22, gpio.OUT)
	gpio.setup(23, gpio.OUT)
	gpio.setup(24, gpio.OUT)

def forward(seconds):
	'''
	Moves the motor conntect to the controller board "forward".

	NOTE: forward is arbitrary and depends on the connection of the + and -
	leads

	:param seconds: The number of seconds to sleep

	'''
	init()
	gpio.output(17, True)
	gpio.output(22, False)
	gpio.output(23, True)
	gpio.output(24, False)
	time.sleep(seconds)
	gpio.cleanup()

def backward(seconds):
	'''
	Moves the motor conntect to the controller board "backward".

	NOTE: backward is arbitrary and depends on the connection of the + and -
	leads

	:param seconds: The number of seconds to sleep

	'''

	init()
	gpio.output(17, False)
	gpio.output(22, True)
	gpio.output(23, False)
	gpio.output(24, True)
	time.sleep(seconds)
	gpio.cleanup()

# Configuration settings for Firebase
# These settings determine which database is connected
config = {
	"apiKey": "AIzaSyC3tcDJPD4nXPslkhZ7gscE8p9Im4Gw00s",
	"authDomain": "easy-lock.firebaseapp.com",
  	"databaseURL": "https://easy-lock.firebaseio.com/",
  	"storageBucket": "easy-lock.appspot.com"
}

firebase = pyrebase.initialize_app(config)	# initialize the firebase variable
db = firebase.database()					# initialize the Firebase database
storage = firebase.storage()				# initialize the storage database

def stream_handler(data):
	'''
	Handles the data stream from Firebase. Locks and unlocks the door.

	:param message: the data from Firebase

	'''

	print(data["path"])
	print(data["data"])
	print(data["event"])
	if data["event"] == 'patch':
		if data["data"].get("status", None) is True:
			backward(2.5) # lock door, less than unlock to fix mechanical bug
		else:
			forward(2.7) # unlock door




lock_firebase_stream = db.child("doors/door1").stream(stream_handler)
