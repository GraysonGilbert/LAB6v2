import time
import RPi.GPIO as GPIO
import multiprocessing
from led8x8 import LED8x8

display = LED8x8(data=23, latch=24, clock=25)  #initializes the display

try:
	smileProcess = multiprocessing.Process(target=display.randomWalk)  #starts the randomWalk process
	smileProcess.start()
except:  #breaks out of loop
	pass
smileProcess.terminate()  #ends the process
smileProcess.join()
GPIO.cleanup()  # cleanups up GPIO ports

