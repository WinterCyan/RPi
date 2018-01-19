#!/usr/bin/python3
#WASDRL button

import time
import RPi.GPIO as IO
import uinput

UP=15;DOWN=22;LEFT=18;RIGHT=13;BTN1=11;BTN2=7
KEY=[UP,DOWN,LEFT,RIGHT,BTN1,BTN2]
EVENT=[uinput.KEY_UP,uinput.KEY_DOWN,uinput.KEY_LEFT,uinput.KEY_RIGHT,uinput.KEY_ENTER,uinput.KEY_ENTER]

def gpio_init():
	IO.setmode(IO.BOARD)
	for key in KEY:
		IO.setup(key,IO.IN,pull_up_down=IO.PUD_UP)

def main():
	gpio_init()
	device=uinput.Device(EVENT)
	time.sleep(2)
	print('KEY ready!')

	btn_state=[False,False,False,False,False,False]
	key_state=[False,False,False,False,False,False]		# like a protect lock

	while True:
		for idx,val in enumerate(KEY):
			if IO.input(val)==False:btn_state[idx]=True
			else:btn_state[idx]=False
		for idx,val in enumerate(btn_state):
			if val and key_state[idx]==False:
				device.emit(EVENT[idx],1)
				key_state[idx]=True
			elif val==False and key_state[idx]:
				device.emit(EVENT[idx],0)
				key_state[idx]=False
		time.sleep(0.1)

try:
	main()
finally:
	IO.cleanup()
