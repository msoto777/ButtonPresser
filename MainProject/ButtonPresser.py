"""Control a single digital GPIO output on a Raspberry Pi 4.

The relay is active-HIGH: driving the GPIO to 3.3V energizes the coil,
driving it LOW de-energizes it.
"""

import RPi.GPIO as GPIO


class ButtonPresser:
    DEFAULT_PIN = 17

    def __init__(self, pin: int = DEFAULT_PIN):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW)

    def outputOn(self) -> None:
        GPIO.output(self.pin, GPIO.HIGH)

    def outputOff(self) -> None:
        GPIO.output(self.pin, GPIO.LOW)

    def cleanup(self) -> None:
        GPIO.cleanup(self.pin)


if __name__ == "__main__":
    import time

    presser = ButtonPresser()
    try:
        presser.outputOn()
        time.sleep(1)
        presser.outputOff()
    finally:
        presser.cleanup()
