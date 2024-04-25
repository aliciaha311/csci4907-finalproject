import time
from servo import Servo
from machine import Pin

soundSpeed = 340 # speed of sound
trigDuration_US = 10 # trig duration
detectionDistance = 0 # detection distance

# ultrasound sensor
TRIG = Pin(23, Pin.OUT)
ECHO = Pin(36, Pin.IN)

# servo
mini_servo = Servo(15)

def move_servo():
    mini_servo.move(90)
    time.sleep(0.7)
    mini_servo.move(0)
    time.sleep(0.3)

# calculates distance in centimeters
def distance_calc():
    TRIG.value(0)
    time. sleep_us(2)
    TRIG.value(1)
    time.sleep_us(trigDuration_US)
    TRIG.value(0)
    
    while ECHO.value() == 0:
        time1 = time.ticks_us()
    while ECHO.value() == 1:
        time2 = time.ticks_us()
    
    during = (time2 - time1) / 1000000
    time.sleep_ms(500)
    return during * soundSpeed / 2 * 100 # returns distance in centimeters

'''
try:
    while True:
        distance_calc()
        detectionDistance = distance_calc()
        print("Distance: " + str(detectionDistance))
        if detectionDistance < 10:
            move_servo()
except KeyboardInterrupt:
    print("Program stopped")
'''
