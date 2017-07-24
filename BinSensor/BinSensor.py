import RPi.GPIO as GPIO
import time
import Email

GPIO.setmode(GPIO.BCM)
BinNo = 1

#BCM Pin 23 == Pin 16 on header. Switch to be connected to pin 16 and 3.3v pin
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#This function will run when the button is triggered
def EmailFunction():
  print(“Button Triggered - Bin is full!”)
  SendEmail("craighissett@gmail.com", 'Bin ' + str(BinNo) + ' is full', "Please proceed")
  print("Trigger 30min delay")
  time.sleep(30)
  
GPIO.add_event_detect(23, GPIO.RISING, callback=EmailFunction, bouncetime=300)

GPIO.cleanup()
