#!/usr/bin/python3
#respond to button

import time
import RPi.GPIO as IO
import os

pin_in=11

def pin_init():
	IO.setmode(IO.BOARD)
	IO.setup(pin_in,IO.IN,pull_up_down=IO.PUD_UP)
	
def main():
	pin_init()
	count=0
	push=True	#control lock
	while True:
		val=IO.input(pin_in)
		if val and push:
			print('OPEN')
			push=False
		elif val==False and push==False:
			count=count+1
			print('CLOSE %s' %str(count))
			os.system("flite -t %s" %count)
			push=True
	time.sleep(0.001)
	   
try:
	main()
finally:
	IO.cleanup()
