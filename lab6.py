import time
import RPi.GPIO as GPIO
import multiprocessing
from led8x8 import LED8x8

display = LED8x8(data=23, latch=24, clock=25)  #initializes the display

try:
	lightProcess = multiprocessing.Process(target=display.randomWalk)  #starts the randomWalk process
	lightProcess.start()
	while 1:
		time.sleep(1)
except:  #breaks out of loop
	pass
lightProcess.terminate()  #ends the process
lightProcess.join()
GPIO.cleanup()  # cleanups up GPIO ports

