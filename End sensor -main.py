from microbit import *
from ultrasonic import Ultrasonic
import radio
import time
radio.config(group=21)
radio.on()
S = 0
a = 0
d = 0.3
ultrasonic_sensor = Ultrasonic()
while True:
    mes = radio.receive()
    print(mes)
    if mes == '1':
        a = 1
    if a == 1:
        S += 1
        sleep (100)
        distance_value = ultrasonic_sensor.measure_distance_cm()
        if distance_value < 50:
            S = S/10
            V = d/S
            if V <0.5 :
                pin0.write_digital(0)
            if V >0.5:
                pin0.write_digital(1)
            a=0
            s=0