#!/usr/bin/python3
import RPi.GPIO as IO
import time

RS=7;EN=8;D4=25;D5=24;D6=23;D7=18;ON=15

width=20
char=True
cmd=False

line1=0x80
line2=0xC0
line3=0x94
line4=0xD4

pulse=0.0005
delay=0.0005

def main():
	IO.setmode(IO.BCM)
	IO.setup(EN,IO.OUT)
	IO.setup(RS,IO.OUT)
	IO.setup(D4,IO.OUT)
	IO.setup(D5,IO.OUT)
	IO.setup(D6,IO.OUT)
	IO.setup(D7,IO.OUT)
	IO.setup(ON,IO.OUT)

	lcd_init()

	lcd_backlight(True)
	time.sleep(0.5)
	lcd_backlight(False)
	time.sleep(0.5)
	lcd_backlight(True)
	time.sleep(0.5)

	while True:
		lcd_string("---------------",line1,2)
		lcd_string("Raspberry Pi",line2,1)
		lcd_string("Winter Cyan",line3,1)
		lcd_string("LCD module test",line4,3)

		time.sleep(3)

		lcd_string("From raspi-spy",line1,2)
		lcd_string("THANKS!",line2,1)
		lcd_string("",line3,1)
		lcd_string("LCD module test",line4,3)

		time.sleep(3)

def lcd_init():
	lcd_byte(0x33,cmd)
	lcd_byte(0x32,cmd)
	lcd_byte(0x06,cmd)
	lcd_byte(0x0C,cmd)
	lcd_byte(0x28,cmd)
	lcd_byte(0x01,cmd)
	time.sleep(delay)


def lcd_byte(bits,mode):
	IO.output(RS,mode)

	IO.output(D4,False)
	IO.output(D5,False)
	IO.output(D6,False)
	IO.output(D7,False)

	if bits&0x10==0x10:IO.output(D4,True)
	if bits&0x20==0x20:IO.output(D5,True)
	if bits&0x40==0x40:IO.output(D6,True)
	if bits&0x80==0x80:IO.output(D7,True)

	lcd_toggle_enable()


	IO.output(D4,False)
	IO.output(D5,False)
	IO.output(D6,False)
	IO.output(D7,False)

	if bits&0x01==0x01:IO.output(D4,True)
	if bits&0x02==0x02:IO.output(D5,True)
	if bits&0x04==0x04:IO.output(D6,True)
	if bits&0x08==0x08:IO.output(D7,True)

	lcd_toggle_enable()


def  lcd_toggle_enable():
	time.sleep(delay)
	IO.output(EN,True)
	time.sleep(pulse)
	IO.output(EN,False)
	time.sleep(delay)


def lcd_backlight(flag):
	IO.output(ON,flag)


def lcd_string(msg,line,style):
	if style==1:
		msg=msg.ljust(width," ")
	elif style==2:
		msg=msg.center(width," ")
	elif style==3:
		msg=msg.rjust(width," ")

	lcd_byte(line,cmd)                

	for i in range(width):
		lcd_byte(ord(msg[i]),char)


if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass
	finally:
		lcd_byte(0x01,cmd)
		lcd_string("Bye...",line4,3)
		IO.cleanup()
