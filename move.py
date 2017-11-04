import RPi.GPIO as gpio		# Used to connect to Raspberry Pi
import time					# Used to sleep main thread for lock


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

forward(0.2)
