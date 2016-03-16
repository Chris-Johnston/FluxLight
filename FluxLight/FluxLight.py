import KelvinColor as kelvin
import time
import datetime
import Lightbulb as light
import math

light.IP = "192.168.2.37"

K_MAX = 6500
K_MIN = 2000
HOUR_OFFSET = 13 + 2 # what hour is the middle of the day (bluest)

UPDATE_DELAY = 30 * 60 # update every 30 minutes
frequency = 60 * 60 * 24 # number of seconds in 1 day, don't change this unless you want a <24hr frequency

light.connect()
# startup sequence, to show that it works
light.setColor(kelvin.toRGB(K_MAX))
time.sleep(3)
light.setColor(kelvin.toRGB(K_MIN))
time.sleep(3)
#light.setColor((0, 0, 0))
#time.sleep(5)

if __name__ == "__main__":

	while True:
		k = K_MIN  + (K_MAX - K_MIN) / 2 
		k = k + (K_MAX - K_MIN) / 2 * math.sin(((time.time() * 2 * math.pi) / frequency) - ((math.pi * 2 * HOUR_OFFSET * 60 * 60) / frequency))
		print(str(k) + " kelvin")
		light.setColor(kelvin.toRGB(k))
		time.sleep(UPDATE_DELAY)