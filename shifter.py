# This code is exactly what was given, no modifications
import RPi.GPIO as GPIO
import time

class Shifter:
  def __init__(self, dataPin, latchPin, clockPin):
    self.dataPin = dataPin
    self.latchPin = latchPin
    self.clockPin = clockPin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.dataPin, GPIO.OUT)
    GPIO.setup(self.latchPin, GPIO.OUT, initial=0)  # start latch & clock low
    GPIO.setup(self.clockPin, GPIO.OUT, initial=0)  

  def ping(self, pin):
    GPIO.output(pin,1)  # ping the clock pin to shift register data
    time.sleep(0)
    GPIO.output(pin,0)

  def shiftByte(self, byteVal):
    for i in range(8):          # 8 bits in pattern
      #GPIO.output(self.dataPin, byteVal & (1<<i)) 
      GPIO.output(self.dataPin, ~(byteVal & (1<<i)))  # if common anode
      self.ping(self.clockPin)

  def latch(self):
    self.ping(self.latchPin)