import board
import neopixel
import time

from colour import Color

NUM_PIXELS = 36

pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS, auto_write=False, pixel_order=neopixel.GRB)

def clear():
    for idx in range(0, NUM_PIXELS):
        pixels[idx] = (0, 0, 0)

gamma = [
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,
    1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,
    2,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  5,  5,  5,
    5,  6,  6,  6,  6,  7,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10,
    10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16,
    17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 24, 25,
    25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36,
    37, 38, 39, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50,
    51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68,
    69, 70, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89,
    90, 92, 93, 95, 96, 98, 99,101,102,104,105,107,109,110,112,114,
    115,117,119,120,122,124,126,127,129,131,133,135,137,138,140,142,
    144,146,148,150,152,154,156,158,160,162,164,167,169,171,173,175,
    177,180,182,184,186,189,191,193,196,198,200,203,205,208,210,213,
    215,218,220,223,225,228,231,233,236,239,241,244,247,249,252,255
]

def apply_gamma(color):
    r = gamma[int(color[0])]
    g = gamma[int(color[1])]
    b = gamma[int(color[2])]
    return (r, g, b)

colors_A = [
    (63, 0, 0),
    (0, 63, 0),
    (0, 0, 63),
    (63, 63, 0),
    (31, 31, 0),
    (31, 15, 31),
    (64, 0, 64),
    (127, 64, 0),
    (0, 64, 127),
    (127, 0, 64),
    (127, 127, 127),
    (32, 32, 32),
    (32, 32, 0),
    (32, 64, 127),
    (127, 32, 127),
    (255, 0, 0),
    (0, 255, 32),
    (32, 0, 255),
    (63, 0, 0),
    (0, 63, 0),
    (0, 0, 15),
    (7, 7, 0),
    (7, 15, 0),
    (15, 7, 15),
    (3, 0, 3),
    (7, 3, 0),
    (0, 64, 127),
    (127, 0, 64),
    (127, 127, 127),
    (32, 32, 32),
    (32, 32, 0),
    (32, 64, 127),
    (127, 32, 127),
    (255, 0, 0),
    (0, 255, 32),
    (32, 0, 255)
]

colors_B = [
    (1.0, 1.0, 1.0),
    (1.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, 0.0, 1.0)
]

modes = ['A', 'B', 'C', 'D']

mode = modes[1]

try:
    if mode == 'A':
        pos = 0
        while True:
            clear()
            idx = pos
            for x in range(0,NUM_PIXELS):
                pixels[idx] = colors_A[x]
                #pixels[idx] = colors_A[x]
                idx = idx + 1
                if idx > (NUM_PIXELS - 1):
                    idx = idx - NUM_PIXELS

            pos = pos + 1
            if pos > (NUM_PIXELS - 1):
                pos = pos - NUM_PIXELS
            pixels.show()
            time.sleep(0.05)
    elif mode == 'B':
        color_index = 0
        brightness = 0
        direction = 5

        hue = colors_B[color_index]
        while True:
            clear()
            color = (hue[0]*brightness, hue[1]*brightness, hue[2]*brightness)
            for idx in range(0, NUM_PIXELS):
                pixels[idx] = color
            pixels.show()

            brightness = brightness + direction
            if brightness > 255:
                brightness = 255
                direction = -5
            elif brightness < 0:
                brightness = 0
                direction = 5
                color_index = color_index + 1
                if color_index > len(colors_B)-1:
                    color_index = 0
                hue = colors_B[color_index]

            time.sleep(0.1)
    elif mode == 'C':
        pos = 0
        color_index = 0
        hue = colors_B[color_index]
        while True:
            clear()
            for idx in range(pos, pos, -1):
                brightness = int(256 - (256.0/NUM_PIXELS)*(pos-idx))
                pixels[idx] = apply_gamma((hue[0]*brightness, hue[1]*brightness, hue[2]*brightness))
            for idx in range(pos, 18-pos, 1):
                brightness = int(256 - (256.0/NUM_PIXELS)*(idx-pos))
                pixels[idx] = apply_gamma((hue[0]*brightness, hue[1]*brightness, hue[2]*brightness))
            pixels.show()
            pos = pos + 1
            if pos > (NUM_PIXELS-1):
                pos = 0
            time.sleep(0.1)
    elif mode == 'D':
        while True:
            clear()
            for idx in range(0, NUM_PIXELS):
                pixels[idx] = apply_gamma(255, 255, 127)
            pixels.show()
        time.sleep(1)


except KeyboardInterrupt:
    clear()
    pixels.show()

