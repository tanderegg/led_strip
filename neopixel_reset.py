import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 18, auto_write=False, pixel_order=neopixel.GRB)

for idx in range(0, 18):
    pixels[idx] = (0, 0, 0)

pixels.show()
