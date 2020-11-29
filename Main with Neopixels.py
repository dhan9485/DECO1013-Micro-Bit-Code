from microbit import *
from gesture import *
import neopixel
from random import randint

def range_map(value, in_min, in_max, out_min, out_max):
	return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def pre1(range1, range2):
    red = randint(range1, range2)
    green = randint(range1, range2)
    blue = randint(range1, range2)
    for pixel_id in range(num_pixels):
        np[pixel_id] = (red, green, blue)
        np.show()
        sleep(50)

def pre2(range3, range4):
    red = randint(range3, range4)
    green = randint(range3, range4)
    blue = randint(range3, range4)
    sleep (1000)
    for pixel_id in range(num_pixels):
        np[pixel_id] = (red, green, blue)
        np.show()

def pre3(range5, range6):
    for pixel_id in range(num_pixels):
        red = randint(range5, range6)
        green = randint(range5, range6)
        blue = randint(range5, range6)
        np[pixel_id] = (red, green, blue)
        np.show()

num_pixels = 30
np = neopixel.NeoPixel(pin0, num_pixels)

gesture = Gesture()

clockwise = Image("99999:""00009:""09009:""99990:""09000:")
anticlockwise = Image("99999:""90000:""90090:""09999:""00090:")
forward = Image("09090:""99099:""00000:""99099:""09090:")
backward = Image("99099:""90009:""00000:""90009:""99099:")
wave = Image("00090:""99999:""00000:""99999:""09000:")
gesture_map = {
    'up': Image.ARROW_N,
    'down': Image.ARROW_S,
    'left': Image.ARROW_W,
    'right': Image.ARROW_E,
    'forward': forward,
    'backward': backward,
    'clockwise': clockwise,
    'anticlockwise': anticlockwise,
    'wave': wave
}

i = 100
b = 101
a = 100

while True:

    g = gesture.read()

    if g == 'left':
        i -= 1
    if g == 'right':
        i += 1
    if g == 'up':
        b -= 1
    if g == 'down':
        b += 1
    if g == 'clockwise':
        a += 1
    if g == 'anticlockwise':
        a -= 1

    if i % 4 == 1:
        if b % 4 == 0:
            pre1(0, 6)
        if b % 4 == 1:
            pre1(7,19)
        if b % 4 == 2:
            pre1(20, 38)
        if b % 4 == 3:
            pre1(39, 63)

    if i % 4 == 0:
        if b % 4 == 0:
            pre2(0,6)
        if b % 4 == 1:
            pre2(7, 19)
        if b % 4 == 2:
            pre2(20, 38)
        if b % 4 == 3:
            pre2(39, 63)

    if i % 4 == 2:
        if b % 4 == 0:
            pre3(0,6)
        if b % 4 == 1:
            pre3(7, 19)
        if b % 4 == 2:
            pre3(20, 38)
        if b % 4 == 3:
            pre3(39, 63)

    if i % 4 == 3:
        if a % 2 == 0:
            value = pin1.read_analog()
            mapped = range_map(value, 0, 1023, 0, 255)
            m = int(mapped)
            red = randint(0, m)
            green = randint(0, m)
            blue = randint(0, m)
            for pixel_id in range(num_pixels):
                np[pixel_id] = (red, green, blue)
                np.show()
        if a % 2 == 1:
            value = pin1.read_analog()
            mapped = range_map(value, 0, 1023, 0, 255)
            m = int(mapped)
            for pixel_id in range(num_pixels):
                np[pixel_id] = (m, m, m)
                np.show()