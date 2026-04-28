#!/bin/sh
#the LED turns green for 2 seconds and then turns off
green() {
	echo "225" > /sys/class/leds/hub:green:led1/brightness
	sleep 2
	echo "0" > /sys/class/leds/hub:green:led1/brightness
}
#the LED turns yellow for 2 seconds and then turns off
yellow() {
	echo "225" > /sys/class/leds/hub:red:led3/brightness
	echo "225" > /sys/class/leds/hub:green:led1/brightness
	sleep 2
	echo "0" > /sys/class/leds/hub:red:led3/brightness
	echo "0" > /sys/class/leds/hub:green:led1/brightness
}
#the LED turns red for 2 seconds and then turns off
red() {
	echo "225" > /sys/class/leds/hub:red:led3/brightness
	sleep 2
	echo "0" > /sys/class/leds/hub:red:led3/brightness
}
#the LED turns blue for 2 seconds and then turns off
blue() {
	echo "225" > /sys/class/leds/hub:blue:led2/brightness
	sleep 2
	echo "0" > /sys/class/leds/hub:blue:led2/brightness
}
#the LED turns purple for 2 seconds and then turns off
purple() {
	echo "225" > /sys/class/leds/hub:red:led3/brightness
	echo "225" > /sys/class/leds/hub:blue:led2/brightness
	sleep 2
	echo "0" > /sys/class/leds/hub:red:led3/brightness
	echo "0" > /sys/class/leds/hub:blue:led2/brightness
}
#the LED turns white for 2 seconds and then turns off
white() {
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
	white
	red
	purple
	blue
done