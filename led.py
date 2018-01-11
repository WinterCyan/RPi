#!/usr/bin/python3
#led.py

import time
import RPi.GPIO as IO

B=15;R=13;G=11
EN=1;DIS=0
RGB=[B,R,G]
def led_init():
	IO.setmode(IO.BOARD)
	for val in RGB:
		IO.setup(val,IO.OUT)
		
def main():
	led_init()
	for val in RGB:
		IO.output(val,EN)
#		print('%s led on...' %str(val))
		time.sleep(0.001)
		IO.output(val,DIS)
#		print('%s led off...' %str(val))
		
try:
	while(1):
		main()
finally:
	IO.cleanup()
	print('Over.')
