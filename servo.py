import RPi.GPIO as GPIO
import time


def runServo(PIN):

    servoPIN = PIN
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
    p.start(2.5)  # Initialization
    try:
        p.ChangeDutyCycle(7.5)  # turn towards 90 degree
        time.sleep(5)  # sleep 1 second
        p.ChangeDutyCycle(2.5)  # turn towards 0 degree
        time.sleep(1)  # sleep 1 second

    except KeyboardInterrupt:
        p.stop()

    finally:
        GPIO.cleanup()
