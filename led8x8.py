from shifter import Shifter
import time
import multiprocessing
from random import randint

#_____Smiley Face poriton of Code___________
#rows = [0b10000000, 0b01000000, 0b00100000, 0b00010000, 0b00001000, 0b00000100, 0b00000010, 0b00000001]
#pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]


class LED8x8(multiprocessing.Process):

	pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001,0b10100101, 0b10011001, 0b01000010, 0b00111100]  #for smiley face portion of the lab
	multiPattern = multiprocessing.Array('i',8)  #declares a multiprocessing array
	for x in range(8):
		multiPattern[x] = pattern[x]

	def __init__(self, data, latch, clock):
		self.shifter = Shifter(data, latch, clock)
    
    
	def randomWalk(self):
		x = 4  #chose to make starting position (4,4)
		y = 4
		while True:  #keeps the random movement going
			while True:  #loop until acceptable move is chosen
				oldX = x
				oldY = y
				x += randint(-1, 1)
				y += randint(-1, 1)
				if (0 <= x <= 7) and (0 <= y <= 7):  #checks to make sure move was on the board
					break
				else:  #if the move is not acceptable, it will reset values and randomly change again
					x = oldX
					y = oldY
			self.shifter.shiftByte(( 1 << x))  #selects one LED to be lit up at the desired location
			self.shifter.shiftByte(~(1 << y))
			self.shifter.ping(self.shifter.latchPin)
			time.sleep(.1)  #delay of .1 seconds as requested
      
#____________Smiley Face portion of Code_______________
#  def display(self,num):
#    global pattern
#    global rows
#    self.shifter.shiftByte(rows[num])
#    self.shifter.shiftByte(pattern[num])
#    self.shifter.pingLatch() #ping latch    
#    time.sleep(.001)
