# script to blink LED's two at a time for Bryce and Naz's bush outside during halloween

import time
import random


class BushEyes:
    pin = 0

    def __init__(self, pin):
        self.pin = pin


class PinManager:
    def unexport_pin(self, pin):
        f = open('/sys/class/gpio/unexport', 'w')
        f.write(str(pin))
        f.close()

    def export_pin(self, pin):
        f = open('/sys/class/gpio/export', 'w')
        f.write(str(pin))
        f.close()

    def define_direction(self, pin, direction):
        path = '/sys/class/gpio/gpio' + str(pin) + '/direction'
        f = open(path, 'w')
        f.write(str(direction))
        f.close()

    def set_pin_value(self, pin, value):
        path = '/sys/class/gpio/gpio' + str(pin) + '/value'
        f = open(path, 'w')
        f.write(str(value))
        f.close()


# Use the following GPIOs for LEDs
eyesList = [BushEyes(2),
            BushEyes(3),
            BushEyes(4),
            BushEyes(24),
            BushEyes(25),
            BushEyes(7),
            BushEyes(8),
            BushEyes(9),
            BushEyes(10),
            BushEyes(11),
            BushEyes(14),
            BushEyes(15),
            BushEyes(17),
            BushEyes(18),
            BushEyes(27)]

# Create a pin manager to help us write pin values and directions
pinMgr = PinManager()

for eyes in eyesList:
    pinMgr.unexport_pin(eyes.pin)
    pinMgr.export_pin(eyes.pin)
    pinMgr.define_direction(eyes.pin, 'out')

random = random.Random()

while 1:
    index = random.randint(0, len(eyesList) - 1)
    pinMgr.set_pin_value(eyesList[index].pin, 1)
    time.sleep(1)
    pinMgr.set_pin_value(eyesList[index].pin, 0)
    time.sleep(0.5)

for eyes in eyesList:
    pinMgr.unexport_pin(eyes.pin)
