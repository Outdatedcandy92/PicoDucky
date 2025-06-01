# PicoDucky V2.0

PicoDucky Version 2.0 is a minimalist, USB-stick-style RP2350 board designed to be used as a security key or as a rubber ducky.

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/ae970f0a6f5bb1eed9011fdd2f88bf826c3ecb2c_image.png)


All the source file for this board are located in `/src/V2.0`


## 🔧 Features

- RP2350 Microcontroller
- Plug-and-play USB-A form factor
- Compact Size 
- 1 Programmable Button
- 2 Programmable RGB LEDs
- Can act like a HID Device
- Can be used as a Security Key

## 📐 Schematic & PCB
![IMG](https://hc-cdn.hel1.your-objectstorage.com/s/v3/9a598c98e71bae9ca623dc363c0f05c66eb1a79a_image.png)
![IMG](https://hc-cdn.hel1.your-objectstorage.com/s/v3/29afcae914f33e2b16b359cace18a4e01a88d22d_image.png)
![IMG](https://hc-cdn.hel1.your-objectstorage.com/s/v3/b4b3f82e9c5ca1cb7696126d628875e0a9d8d85d_image.png)


##  🚀 Getting Started

### As a HID Device

1. Hold `BOOT` button while plugging in the board
2. Download and then drag and drop the `.uf2` from [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/)
3. Press the `RESET` button or replug the usb back into the board
4. Download adafruit circuit python bundle from [here](https://circuitpython.org/libraries)
5. Extract the bundle and find `adafruit-hid` folder inside the `lib` folder
6. Copy `adafruit-hid` folder and paste it into the CIRCUITPY `lib` folder.
7. Open `code.py` and write your own code or copy the demo code from the repo `./code/code.py`
8. All done!

### As a Security Key

1. Go to the [PicoFIDO getting started page](https://www.picokeys.com/getting-started/).
2. Download the Pico FIDO firmware for PicoDucky V2.
3. Hold the `BOOT` button while plugging the board into your computer.
4. Drag and drop the downloaded `.uf2` file onto the device that appears.
5. Unplug and replug the USB to reboot the board.
6. Visit the [Pico Commissioner](https://www.picokeys.com/pico-commissioner/) to commission your security key.


