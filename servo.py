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


def runUpServo(PIN):

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)

    p = GPIO.PWM(PIN, 50)  # GPIO 17 for PWM with 50Hz
    p.start(2.5)  # Initialization
    try:
        p.ChangeDutyCycle(7.5)  # turn towards 90 degree

    except KeyboardInterrupt:
        p.stop()

    finally:
        GPIO.cleanup()


def runDownServo():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)

    p0 = GPIO.PWM(17, 50)  # GPIO 17 for PWM with 50Hz
    p1 = GPIO.PWM(22, 50)  # GPIO 22 for PWM with 50Hz
    p2 = GPIO.PWM(27, 50)  # GPIO 27 for PWM with 50Hz

    p0.start(2.5)  # Initialization
    p1.start(2.5)  # Initialization
    p2.start(2.5)  # Initialization

    GPIO.cleanup()
