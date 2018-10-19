import RPi.GPIO as gpio
import time

port_num1 = 7
port_num2 = 11

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)


gpio.setup(port_num1, gpio.OUT)
gpio.setup(port_num2, gpio.OUT)

for i in range(100):
    gpio.setup(port_num1, gpio.OUT)
    gpio.setup(port_num2, gpio.OUT)
    gpio.output(port_num1, 0)
    time.sleep(0.1)
    gpio.output(port_num2, 0)
    time.sleep(0.1)
    gpio.output(port_num1, 1)
    time.sleep(0.1)
    gpio.output(port_num2, 1)
    time.sleep(0.1)
    print(i)
    if 1 == i%5:
        time.sleep(3)