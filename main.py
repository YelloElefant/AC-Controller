from machine import Pin
onboard_led = Pin("LED", Pin.OUT)
onboard_led.value(1)