import RPi.GPIO as GPIO
import time
from bottle import route, run, template, static_file

fl_r = 18
fl_b = 23

fr_r = 20
fr_b = 21

bl_r = 17
bl_b = 4

br_r = 27
br_b = 22


@route('/static/<filename>')
def static(filename):
	return static_file(filename, root='./static/')

@route('/')
def index():
	return template('cntlr')

@route('/stop')
def stop():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([fl_r,fl_b,fr_r,fr_b], GPIO.OUT)
        GPIO.setup([bl_r,bl_b,br_r,br_b], GPIO.OUT)

        GPIO.output(fl_r, False)
        GPIO.output(fl_b, False)
        GPIO.output(fr_r, False)
        GPIO.output(fr_b, False)

        GPIO.output(bl_r, False)
        GPIO.output(bl_b, False)
        GPIO.output(br_r, False)
        GPIO.output(br_b, False)

        GPIO.cleanup()


@route('/up/<state>')
def up(state):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup([fl_r,fl_b,fr_r,fr_b], GPIO.OUT)
	GPIO.setup([bl_r,bl_b,br_r,br_b], GPIO.OUT)

	if(state == 'on'):
		GPIO.output(fl_r, False)
		GPIO.output(fl_b, True)
		GPIO.output(fr_r, True)
		GPIO.output(fr_b, False)

		GPIO.output(bl_r, True)
		GPIO.output(bl_b, False)
		GPIO.output(br_r, False)
		GPIO.output(br_b, True)
	else:
		GPIO.cleanup()

@route('/left/<state>')
def left(state):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([fl_r,fl_b,fr_r,fr_b], GPIO.OUT)
        GPIO.setup([bl_r,bl_b,br_r,br_b], GPIO.OUT)
	if(state == 'on'):
	        GPIO.output(fl_r, True)
	        GPIO.output(fl_b, False)
	        GPIO.output(fr_r, True)
	        GPIO.output(fr_b, False)

	        GPIO.output(bl_r, False)
	        GPIO.output(bl_b, True)
	        GPIO.output(br_r, False)
	        GPIO.output(br_b, True)

	else:
	        GPIO.cleanup()

@route('/right/<state>')
def right(state):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([fl_r,fl_b,fr_r,fr_b], GPIO.OUT)
        GPIO.setup([bl_r,bl_b,br_r,br_b], GPIO.OUT)
	if(state == 'on'):
	        GPIO.output(fl_r, False)
	        GPIO.output(fl_b, True)
	        GPIO.output(fr_r, False)
	        GPIO.output(fr_b, True)

	        GPIO.output(bl_r, True)
	        GPIO.output(bl_b, False)
	        GPIO.output(br_r, True)
	        GPIO.output(br_b, False)

	else:
	        GPIO.cleanup()

@route('/down/<state>')
def down(state):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([fl_r,fl_b,fr_r,fr_b], GPIO.OUT)
        GPIO.setup([bl_r,bl_b,br_r,br_b], GPIO.OUT)
	if(state == 'on'):
	        GPIO.output(fl_r, True)
	        GPIO.output(fl_b, False)
	        GPIO.output(fr_r, False)
	        GPIO.output(fr_b, True)

	        GPIO.output(bl_r, False)
	        GPIO.output(bl_b, True)
	        GPIO.output(br_r, True)
	        GPIO.output(br_b, False)

	else:
	        GPIO.cleanup()

run(host='192.168.10.1',port=80)
