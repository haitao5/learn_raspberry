import RPi.GPIO as gpio
import time

port_num = 7

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)


gpio.setup(port_num, gpio.OUT)

for i in range(100):
    gpio.setup(port_num, gpio.OUT)
    gpio.output(port_num, 0)
    time.sleep(0.1)
    gpio.output(port_num, 1)
    time.sleep(0.1)
    print(i)
    if 1 == i%5:
        time.sleep(3)