import RPi.GPIO as GPIO
import time


def runServo(PIN):

    servoPIN = PIN
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
    p.start(0)  # Initialization
    try:
        p.ChangeDutyCycle(0)
        time.sleep(0.15)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.15)
        p.ChangeDutyCycle(10)
        time.sleep(0.15)
        p.ChangeDutyCycle(12.5)
        time.sleep(6)
        p.ChangeDutyCycle(10)
        time.sleep(0.15)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.15)
        p.ChangeDutyCycle(0)
        time.sleep(0.15)

    except KeyboardInterrupt:
        p.stop()

    finally:
        GPIO.cleanup()
