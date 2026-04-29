#!/usr/bin/env python3
import time
import struct

infile_path = "/dev/input/event0"

"""
FORMAT represents the format used by linux kernel input event struct
See https://github.com/torvalds/linux/blob/v5.5-rc5/include/uapi/linux/input.h#L28
Stands for: long int, long int, unsigned short, unsigned short, unsigned int
"""
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)

#open file in binary mode
in_file = open(infile_path, "rb")

value = 0
num = 0

def event(value):
	while value != 1:
		event = in_file.read(EVENT_SIZE)
		(tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)



def green():
	with open("/sys/class/leds/hub:green:led1/brightness", "a") as f:
  		f.write("225")
  	time.sleep(0.02)
  	with open("/sys/class/leds/hub:green:led1/brightness", "a") as f:
  		f.write("0")

def blue():
	with open("/sys/class/leds/hub:blue:led2/brightness", "a") as f:
  		f.write("225")
  	time.sleep(0.02)
  	with open("/sys/class/leds/hub:blue:led2/brightness", "a") as f:
  		f.write("0")

def red():
	with open("/sys/class/leds/hub:red:led3/brightness", "a") as f:
  		f.write("225")
  	time.sleep(0.02)
  	with open("/sys/class/leds/hub:red:led3/brightness", "a") as f:
  		f.write("0")

def white():
	with open("/sys/class/leds/hub:red:led3/brightness", "a") as f:
  		f.write("225")
  	with open("/sys/class/leds/hub:blue:led2/brightness", "a") as f:
  		f.write("225")
  	with open("/sys/class/leds/hub:green:led1/brightness", "a") as f:
  		f.write("225")
  	time.sleep(0.02)
  	with open("/sys/class/leds/hub:red:led3/brightness", "a") as f:
  		f.write("0")
  	with open("/sys/class/leds/hub:blue:led2/brightness", "a") as f:
  		f.write("0")
  	with open("/sys/class/leds/hub:green:led1/brightness", "a") as f:
  		f.write("0")

def purple():
	with open("/sys/class/leds/hub:red:led3/brightness", "a") as f:
  		f.write("225")
  	with open("/sys/class/leds/hub:blue:led2/brightness", "a") as f:
  		f.write("225")
  	time.sleep(0.02)
  	with open("/sys/class/leds/hub:red:led3/brightness", "a") as f:
  		f.write("0")
  	with open("/sys/class/leds/hub:blue:led2/brightness", "a") as f:
  		f.write("0")

def yellow():
	with open("/sys/class/leds/hub:red:led3/brightness", "a") as f:
		f.write("225")
	with open("/sys/class/leds/hub:green:led1/brightness", "a") as f:
  		f.write("225")
  	time.sleep(0.02)
  	with open("/sys/class/leds/hub:red:led3/brightness", "a") as f:
  		f.write("0")
  	with open("/sys/class/leds/hub:green:led1/brightness", "a") as f:
  		f.write("0")

# main program
while num == 0:
	red()

	event(value)
	time.sleep(0.1)
	red()
	time.sleep(0.1)
	red()
	time.sleep(0.1)

	event(value)
	blue()
	time.sleep(0.1)
	blue()
	time.sleep(0.1)
	blue()

	event(value)
	time.sleep(0.1)
	green()
	time.sleep(0.1)
	green()
	time.sleep(0.1)
	green()
	time.sleep(0.1)

	event(value)
	yellow()
	time.sleep(0.1)
	yellow()
	time.sleep(0.1)
	yellow()
	time.sleep(0.1)
