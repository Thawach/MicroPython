from machine import Pin
import utime

red = Pin(15, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)

all_led = [red, yellow, green]

while True:
    for led in all_led:
        led.on()
        utime.sleep_ms(500)
        led.off()
        utime.sleep_ms(500)
        