from microbit import *
from ultrasonic import Ultrasonic
import radio
radio.config(group=21)
ultrasonic_sensor = Ultrasonic()
while True:
    mes = radio.send('1')