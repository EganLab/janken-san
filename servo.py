import RPi.GPIO as GPIO
import time


def runServo(PIN, rotation):
    servoPIN = PIN
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
    p.start(5)  # Initialization
    try:
        p.ChangeDutyCycle(rotation)

    except KeyboardInterrupt:
        p.stop()

    finally:
        GPIO.cleanup()
