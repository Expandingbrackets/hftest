#!/bin/sh
green() {
	echo "225" > /sys/class/leds/hub:green:led1/brightness
	sleep 2
	echo "0" > /sys/class/leds/hub:green:led1/brightness
}

yellow() {
	echo "225" > /sys/class/leds/hub:red:led3/brightness
	echo "225" > /sys/class/leds/hub:green:led1/brightness
	sleep 2
	echo "0" > /sys/class/leds/hub:red:led3/brightness
	echo "0" > /sys/class/leds/hub:green:led1/brightness
}

red() {
	echo "225" > /sys/class/leds/hub:red:led3/brightness
	sleep 2
	echo "0" > /sys/class/leds/hub:red:led3/brightness
}

blue() {
	echo "225" > /sys/class/leds/hub:blue:led2/brightness
	sleep 2
	echo "0" > /sys/class/leds/hub:blue:led2/brightness
}

purple() {
	echo "225" > /sys/class/leds/hub:red:led3/brightness
	echo "225" > /sys/class/leds/hub:blue:led2/brightness
	sleep 2
	echo "0" > /sys/class/leds/hub:red:led3/brightness
	echo "0" > /sys/class/leds/hub:blue:led2/brightness
}

pink() {
	echo "225" > /sys/class/leds/hub:red:led3/brightness
	echo "192" > /sys/class/leds/hub:green:led1/brightness
	echo "203" > /sys/class/leds/hub:blue:led2/brightness
	sleep 2
	echo "0" > /sys/class/leds/hub:red:led3/brightness
	echo "0" > /sys/class/leds/hub:green:led1/brightness
	echo "0" > /sys/class/leds/hub:blue:led2/brightness
}

#main program
for i in seq 1 2; do
	green
	yellow
	pink
	red
	purple
	blue
done