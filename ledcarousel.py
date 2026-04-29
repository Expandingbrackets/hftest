#!/usr/bin/env python3
import time

def green():
	with open("/sys/class/leds/hub:green:led1/brightness", "a") as f:
  		f.write("225")
  	time.sleep(1)
  	with open("/sys/class/leds/hub:green:led1/brightness", "a") as f:
  		f.write("0")

def blue():
	with open("/sys/class/leds/hub:blue:led2/brightness", "a") as f:
  		f.write("225")
  	time.sleep(1)
  	with open("/sys/class/leds/hub:blue:led2/brightness", "a") as f:
  		f.write("0")

def red():
	with open("/sys/class/leds/hub:red:led3/brightness", "a") as f:
  		f.write("225")
  	time.sleep(1)
  	with open("/sys/class/leds/hub:red:led3/brightness", "a") as f:
  		f.write("0")

def white():
	with open("/sys/class/leds/hub:red:led3/brightness", "a") as f:
  		f.write("225")
  	with open("/sys/class/leds/hub:blue:led2/brightness", "a") as f:
  		f.write("225")
  	with open("/sys/class/leds/hub:green:led1/brightness", "a") as f:
  		f.write("225")
  	time.sleep(1)
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
  	time.sleep(1)
  	with open("/sys/class/leds/hub:red:led3/brightness", "a") as f:
  		f.write("0")
  	with open("/sys/class/leds/hub:blue:led2/brightness", "a") as f:
  		f.write("0")

 def yellow():
 	with open("/sys/class/leds/hub:red:led3/brightness", "a") as f:
  		f.write("225")
  	with open("/sys/class/leds/hub:green:led1/brightness", "a") as f:
  		f.write("225")
  	time.sleep(1)
  	with open("/sys/class/leds/hub:red:led3/brightness", "a") as f:
  		f.write("0")
  	with open("/sys/class/leds/hub:green:led1/brightness", "a") as f:
  		f.write("0")

# main program
red()
time.sleep(0.5)
red()
time.sleep(0.5)
red()
time.sleep(0.5)
blue()
time.sleep(0.5)
blue()
time.sleep(0.5)
blue()
time.sleep(0.5)
green()
time.sleep(0.5)
green()
time.sleep(0.5)
green()
time.sleep(0.5)
yellow()
time.sleep(0.5)
yellow()
time.sleep(0.5)
yellow()
time.sleep(0.5)