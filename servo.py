from gpiozero import AngularServo
from time import sleep

servo_pin1 = 18
servo_pin2 = 12

servo1 = AngularServo(servo_pin1, min_angle=0, max_angle=180, min_pulse_width=0.0006, max_pulse_width=0.0024)
servo2 = AngularServo(servo_pin2, min_angle=0, max_angle=180, min_pulse_width=0.0006, max_pulse_width=0.0024)

while True:
    servo1.angle = 0
    sleep(1)
    servo2.angle = 0
    sleep(1)

    servo1.angle = 90
    sleep(1)
    servo2.angle = 90
    sleep(1)

    servo1.angle = 180
    sleep(1)
    servo2.angle = 180
    sleep(1)
