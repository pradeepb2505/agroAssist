import RPi.GPIO as GPIO
from time import sleep

# use P1 header pin numbering convention
GPIO.setmode(GPIO.BOARD)

# Set up the GPIO channels
GPIO.setup(11, GPIO.IN) # This could be used to detect a switch
GPIO.setup(12, GPIO.OUT) # This is going to supply the on/off signal

# Output to pin 12. Toggles it on/off every three seconds
while True:
    sleeperTime = 3
    GPIO.output(12, GPIO.LOW)
    sleep(sleeperTime)
    GPIO.output(12, GPIO.HIGH)
    sleep(sleeperTime)

# Input from pin 11
input_value = GPIO.input(11)

