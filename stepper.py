#!/usr/bin/python3
import time
import RPi.GPIO as IO

IN1=14;IN2=15;IN3=18;IN4=23
INs=[IN1,IN2,IN3,IN4]
delay=0.0003
s1=[True,False,False,False];s2=[True,True,False,False];s3=[False,True,False,False];s4=[False,True,True,False]
s5=[False,False,True,False];s6=[False,False,True,True];s7=[False,False,False,True];s8=[True,False,False,True]
steps=[s1,s2,s3,s4,s5,s6,s7,s8]

IO.setmode(IO.BCM)
for pin in INs:
	IO.setup(pin,IO.OUT)

def run(sn):
	for i in range(4):
		IO.output(INs[i],sn[i])
		time.sleep(delay)
		
def main():
	while True:
		for step in steps:
			run(step)

if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('Exit')
	finally:
		for pin in INs:
			IO.output(pin,False)
		IO.cleanup()
