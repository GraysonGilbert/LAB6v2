import time
import RPi.GPIO as GPIO
import multiprocessing
from ledarray import LEDarray

display = LEDarray(data=23, latch=24, clock=25)  #initializes the display

try:
	smileProcess = multiprocessing.Process(target=display.randomWalk)  #starts the randomWalk process
	smileProcess.start()
	while 1:
		print(".")  # Prints a period every second to show that multiprocessing is working
		time.sleep(1)
except:  #breaks out of loop with cntrl-c
	pass
smileProcess.terminate()  #ends the process
smileProcess.join()
GPIO.cleanup()  # cleanups up GPIO
print("done")  # visual confirmation that the above lines were completed
