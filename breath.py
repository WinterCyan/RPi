#!/usr/bin/python3
import time
import RPi.GPIO as GPIO

T=0.01;G=11;R=13;B=15;HIGH=1;LOW=0;peri_length=100
RGB=[R,G,B]

def pin_init():
	GPIO.setmode(GPIO.BOARD)
	for item in RGB:
		GPIO.setup(item,GPIO.OUT)
	
def light_duty(led,period,duty):
	GPIO.output(led,HIGH)
	time.sleep(period*duty)
	GPIO.output(led,LOW)
	time.sleep(period*(1-duty))
	
def breath():
	while(1):
		for item in RGB:
			for i in range(peri_length):
				light_duty(item,T,0.05+i*0.009)
			for i in range(peri_length-1,0,-1):
				light_duty(item,T,0.05+i*0.009)

def main():
	pin_init()
	breath()

try:
	main()
finally:
	GPIO.cleanup()
