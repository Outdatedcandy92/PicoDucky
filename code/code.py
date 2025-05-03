import time
import board
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import usb_hid

# Setup RGB LED 1 (GP15, GP14, GP13)
led1_red = digitalio.DigitalInOut(board.GP15)
led1_green = digitalio.DigitalInOut(board.GP14)
led1_blue = digitalio.DigitalInOut(board.GP13)
led1_red.direction = led1_green.direction = led1_blue.direction = digitalio.Direction.OUTPUT

# Setup RGB LED 2 (GP20, GP19, GP18)
led2_red = digitalio.DigitalInOut(board.GP20)
led2_green = digitalio.DigitalInOut(board.GP19)
led2_blue = digitalio.DigitalInOut(board.GP18)
led2_red.direction = led2_green.direction = led2_blue.direction = digitalio.Direction.OUTPUT

# Setup button on GP17
button = digitalio.DigitalInOut(board.GP17)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP  # Uses internal pull-up resistor

# Create HID keyboard object
keyboard = Keyboard(usb_hid.devices)

def set_color(r1, g1, b1, r2, g2, b2):
    led1_red.value = r1
    led1_green.value = g1
    led1_blue.value = b1
    led2_red.value = r2
    led2_green.value = g2
    led2_blue.value = b2

# Cycle LEDs: red -> green -> blue (LOW = ON)
for _ in range(5):
    set_color(False, True, True, False, True, True)  # Red
    time.sleep(0.1)
    set_color(True, False, True, True, False, True)  # Green
    time.sleep(0.1)
    set_color(True, True, False, True, True, False)  # Blue
    time.sleep(0.1)

# Turn off LEDs
set_color(True, True, True, True, True, True)

print("Ready. Press the button!")

# Loop: wait for button press
while True:
    if not button.value:  # Button is active-low
        print("Button pressed!")

        # Turn on both red LEDs
        set_color(False, True, True, False, True, True)

        # Type "Hello world"
        keys = [
            (Keycode.SHIFT, Keycode.H),  # H
            Keycode.E,
            Keycode.L,
            Keycode.L,
            Keycode.O,
            Keycode.SPACEBAR,
            Keycode.W,
            Keycode.O,
            Keycode.R,
            Keycode.L,
            Keycode.D,
            Keycode.ENTER
        ]

        for key in keys:
            if isinstance(key, tuple):
                keyboard.press(*key)
            else:
                keyboard.press(key)
            keyboard.release_all()
            time.sleep(0.1)
        set_color(False, True, True, False, True, True)

        while not button.value:
            pass  # Wait for button release
        time.sleep(0.05)  # Debounce delay
