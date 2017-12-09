from gpiozero import LEDBoard
from gpiozero import PWMLED
from gpiozero.tools import random_values
from signal import pause
from random import uniform
star = PWMLED(2)
star.blink(fade_in_time=0.25,fade_out_time=0.25)
tree = LEDBoard(*range(3,28),pwm=True)
for led in tree:
    led.blink(on_time=uniform(0.5,3),off_time=uniform(0.5,3),fade_in_time=uniform(0.5,2),fade_out_time=uniform(0.5,1.5))
pause()
