import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
BinNo = 1

#BCM Pin 23 == Pin 16 on header. Switch to be connected to pin 16 and 3.3v pin
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#This function will run when the button is triggered
def EmailFunction():
  print(“Button Triggered - Bin is full!”)
  print(“Send Email here")
  print(Trigger 30min delay)

  
GPIO.add_event_detect(23, GPIO.RISING, callback=EmailFunction, bouncetime=300)

GPIO.cleanup()
