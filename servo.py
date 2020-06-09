import RPi.GPIO as GPIO
import time


def sunServo(PIN):
    servoPIN = PIN
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
    p.start(5)  # Initialization
    try:
        p.ChangeDutyCycle(12.5)
        time.sleep(1)
        p.ChangeDutyCycle(5)

    except KeyboardInterrupt:
        p.stop()

    finally:
        GPIO.cleanup()
