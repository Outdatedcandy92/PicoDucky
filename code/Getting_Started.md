# PicoDucky Documentation

A minimal RP2350-based USB dev board designed for Human Interface Device (HID) projects such as keyboard emulation, rubber ducky payloads, and automation scripts.

|Function|GPIO|Notes|
|---|---|---|
|**Button**|GP11|User-programmable button|
|**RGB LED 1**|GP12 (Red), GP13 (Green), GP14 (Blue)|Onboard status LED|
|**RGB LED 0**|GP19 (Red), GP20 (Green), GP21 (Blue)|Secondary LED or activity indicator|

# Getting Started Guide (Circuitpython)

## Step 1: Install CircuitPython

1. Download the `.UF2` for the Raspberry Pi Pico 2 (since PicoDucky uses the same chip)
2. Plug in your PicoDucky while holding the BOOTSEL button to enter bootloader mode
3. A drive called `RPI-RP2` should appear in your file explorer
4. Drag and drop the `.UF2` file onto it
5. The PicoDucky will reboot and show up as a new drive called `CIRCUITPY`

You’re now ready to start coding in CircuitPython!

## Step 2: Install Libraries

1. Download the [adafruit circuitpython bundle](https://circuitpython.org/libraries)
2. Unzip it, and copy the following folders from `lib/` to the `lib/` directory on your CIRCUITPY drive:
    1. `adafruit_hid`
    2. `adafruit_rgbled.mpy`

## Step 3: Basic HID Example (Keyboard Emulation)

Create a new file on the CIRCUITPY drive called `code.py`, and paste this:

<aside> 💡

This code only works on windows device :c

</aside>

```python
import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Setup button
button = digitalio.DigitalInOut(board.GP11)
button.switch_to_input(pull=digitalio.Pull.UP)

# Setup keyboard
keyboard = Keyboard(usb_hid.devices)

while True:
    if not button.value:  # Button pressed
        keyboard.send(Keycode.WINDOWS, Keycode.R)  # Open Run dialog
        time.sleep(0.3)
        keyboard.write("notepad\\n")  # Launch Notepad
        time.sleep(1)
        keyboard.write("Hello from PicoDucky!\\n")
        while not button.value:
            pass  # Wait for button release
    time.sleep(0.05)
```

Save your code and then press the programmable button on your board, your PicoDucky will then proceed to open notepad and type `Hello from PicoDucky`

## Step 4: Using the RGB LEDs

We can use the `adafruit_rgbled` library to control the on board RGB LEDs

```python
import time
import board
from adafruit_rgbled import RGBLED

# Define RGB LED 1 (GPIO 12, 13, 14)
led1 = RGBLED(board.GP12, board.GP13, board.GP14, invert_pwm=True)

# Define RGB LED 0 (GPIO 19, 20, 21)
led0 = RGBLED(board.GP19, board.GP20, board.GP21, invert_pwm=True)

while True:
    led1.color = (255, 0, 0)   # LED 1 Red
    led0.color = (0, 255, 0)   # LED 0 Green
    time.sleep(0.5)
    led1.color = (0, 0, 255)   # LED 1 Blue
    led0.color = (255, 255, 0) # LED 0 Yellow
    time.sleep(0.5)
```

By adjusting the brightness of each color, you can mix them to produce nearly any color in the visible spectrum.

An RGB LED uses **additive color mixing**, meaning the more light you add, the brighter and whiter the result becomes.

|Color|Red|Green|Blue|Result|
|---|---|---|---|---|
|🔴 Red|255|0|0|Red|
|🟢 Green|0|255|0|Green|
|🔵 Blue|0|0|255|Blue|
|🟡 Yellow|255|255|0|Red + Green|
|🟣 Magenta|255|0|255|Red + Blue|
|⚪ White|255|255|255|All colors full|
|⚫ Off|0|0|0|All off|

Each color channel (R, G, B) accepts a value between **0 and 255**, where:

- `0` means the LED is off.
- `255` means full brightness.

## Step 5: Expanding Your HID Scripts

CircuitPython’s `adafruit_hid` module supports:

- **Keyboard** → `Keyboard`, `Keycode`
- **Mouse** → `Mouse`
- **Consumer Control** → Volume, Media keys, etc.

Example: Mouse movement

```python
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)
mouse.move(x=100, y=0)
```

## Bonus: Useful Resources

[CircuitPython HID Documentation](https://docs.circuitpython.org/projects/hid/en/latest/)

[Adafruit HID Guide](https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse)

[CircuitPython Absolute Mouse Coordinates](https://circuitpython-absolute-mouse.readthedocs.io/en/latest/)
