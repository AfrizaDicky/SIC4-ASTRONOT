import RPi.GPIO as GPIO
import machine
import time
import gpiozero

GPIO.setmode(BOARD.BCM)
GPIO.setwarnings(False)

analog_pin1 = machine.ADC(17)
analog_pin2 = machine.ADC(27)
relay_udara_in = 22
relay_udara_out = 23
led_red = 24
led_green = 25

GPIO.setup(relay_udara_in, GPIO.OUT)
GPIO.setup(relay_udara_out, GPIO.OUT)


while True:
    sensor_value1 = analog_pin1.read_u16()
    print("Sensor Value :", sensor_value1)
    time.sleep(5)

    sensor_value2 = analog_pin2.read_u16()
    print("Sensor Value :", sensor_value2)
    time.sleep(5)


    if sensor_value1 >= 10000:
        GPIO.output(relay_udara_in, GPIO.HIGH)
        time.sleep(15)
        led_green.on()
        time.sleep(15)
        led_green.off()
    
    else:
        GPIO.output(relay_udara_in, GPIO.LOW)
        led_red.on()


    if sensor_value2 <= 6000:
        GPIO.output(relay_udara_out,GPIO.HIGH)
        time.sleep(15)

    else:
        GPIO.output(relay_udara_out, GPIO.LOW)

