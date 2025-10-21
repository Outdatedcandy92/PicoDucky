"""
PicoDucky All-Features Example
Demonstrates HID Keyboard, Mouse, RGB LEDs, and Button.
(Yes I vibecoded ts)

"""

import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
from adafruit_rgbled import RGBLED

# -----------------------------
# Pin Definitions
# -----------------------------
BUTTON_PIN = board.GP11

# RGB LED 1 (Status)
LED1_R = board.GP12
LED1_G = board.GP13
LED1_B = board.GP14

# RGB LED 0 (Activity)
LED0_R = board.GP19
LED0_G = board.GP20
LED0_B = board.GP21

# -----------------------------
# Hardware Setup
# -----------------------------
# Button
button = digitalio.DigitalInOut(BUTTON_PIN)
button.switch_to_input(pull=digitalio.Pull.UP)

# LEDs
led1 = RGBLED(LED1_R, LED1_G, LED1_B, invert_pwm=True)
led0 = RGBLED(LED0_R, LED0_G, LED0_B, invert_pwm=True)

# HID Devices
keyboard = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)


# -----------------------------
# Helper Functions
# -----------------------------

def led_set(color1, color0):
    """Set both RGB LEDs."""
    led1.color = color1
    led0.color = color0


def blink_leds(color1, color0, duration=0.2, times=2):
    """Blink both LEDs."""
    for _ in range(times):
        led_set(color1, color0)
        time.sleep(duration)
        led_set((0, 0, 0), (0, 0, 0))
        time.sleep(duration)


def keyboard_demo():
    """Send a simple keyboard payload."""
    print("Keyboard demo: Opening Notepad and typing text...")
    led_set((0, 0, 255), (0, 0, 255))  # Blue while typing
    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.3)
    keyboard.write("notepad\n")
    time.sleep(1)
    keyboard.write("Hello from PicoDucky!\n")
    blink_leds((0, 255, 0), (0, 255, 0), duration=0.1, times=3)  # Green success blink


def mouse_demo():
    """Move the mouse in a small square."""
    print("Mouse demo: Moving cursor in a square...")
    led_set((255, 255, 0), (255, 255, 0))  # Yellow while moving
    for _ in range(4):
        mouse.move(x=50)
        time.sleep(0.2)
        mouse.move(y=50)
        time.sleep(0.2)
        mouse.move(x=-50)
        time.sleep(0.2)
        mouse.move(y=-50)
        time.sleep(0.2)
    blink_leds((0, 255, 255), (0, 255, 255), duration=0.1, times=2)  # Cyan done


def idle_animation():
    """Soft LED breathing animation while idle."""
    for i in range(0, 256, 5):
        led_set((i, 0, 50), (0, 50, i))
        time.sleep(0.01)
    for i in range(255, -1, -5):
        led_set((i, 0, 50), (0, 50, i))
        time.sleep(0.01)


# -----------------------------
# Main Loop
# -----------------------------
print("PicoDucky All-Features Demo Started.")
led_set((0, 0, 0), (0, 0, 0))

while True:
    if not button.value:  # Button pressed
        led_set((255, 0, 0), (255, 0, 0))  # Red indicates action start
        keyboard_demo()
        mouse_demo()
        led_set((0, 255, 0), (0, 255, 0))  # Green indicates done
        while not button.value:
            pass  # Wait for release
    else:
        idle_animation()
