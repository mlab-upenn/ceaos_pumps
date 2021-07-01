import Rpi.GPIO as GPIO
import time

class Pump():
    def __init__(self):
        self.name = None
        self.pin = None

    
    def set_name(self, name):
        self.name = str(name)
    
    def set_pin(self, pin):
        try: 
            float(pin)
            if pin.is_integer() and pin > 0 and pin <= 26:
                self.pin = pin
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, GPIO.LOW)
        except ValueError:
            print("Must be a valid integer")

    def dispense(self, t):
        if self.pin is not None:
            GPIO.output(self.pin, GPIO.HIGH)
            time.sleep(t)
            GPIO.output(self.pin, GPIO.LOW)
        else:
            print("Must set GPIO pin for %s" % self.name)

    
    