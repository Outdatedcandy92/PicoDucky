# PicoDucky V2.1

PicoDucky Version 2.1 is a minimalist, USB-stick-style RP2350 board designed for use as a security key or rubber ducky.

![image](./attachments/Image.jpg)

All source files for this board are located in `/src/V2.1`.

## Demo

[pd-usb-uvc](https://github.com/JBlitzar/pd-usb-uvc?tab=readme-ov-file) A UVC webcam implementation running on the Picoducky.

![uvc demo](./attachments/demo.mp4)

## Features

- RP2350 Microcontroller
- Plug-and-play USB-A form factor
- Compact size 
- 1 programmable button
- 2 programmable RGB LEDs
- HID device capability
- Security key functionality

## Schematic & PCB

![image](./attachments/schematic.png)

![image](./attachments/pcb.png)

## Getting Started

### As a HID Device

1. Hold the `BOOT` button while plugging in the board
2. Download and drag-and-drop the `.uf2` file from [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/)
3. Press the `RESET` button or replug the USB cable
4. Download the Adafruit CircuitPython bundle from [here](https://circuitpython.org/libraries)
5. Extract the bundle and locate the `adafruit-hid` folder inside the `lib` directory
6. Copy the `adafruit-hid` folder to the CIRCUITPY `lib` directory
7. Open `code.py` and write your own code or copy the demo code from `./code/code.py`
8. You're all set!

### As a Security Key

1. Visit the [PicoFIDO getting started page](https://www.picokeys.com/getting-started/)
2. Download the Pico FIDO firmware for PicoDucky V2
3. Hold the `BOOT` button while plugging the board into your computer
4. Drag-and-drop the downloaded `.uf2` file onto the device that appears
5. Unplug and replug the USB to reboot the board
6. Visit the [Pico Commissioner](https://www.picokeys.com/pico-commissioner/) to commission your security key

## Reproduction Cost and Ordering Guide

When ordering through JLCPCB, several configurations are available with varying costs depending on component selection and assembly requirements. Pricing below assumes ordering 5 PCBs with 2 assembled.

All the required files for production can be found under `/src/{revision}/Production`

### Cheapest Option
*Not bad, but not the best option*

- 1.6mm board thickness
- Green color
- HASL (leaded/lead-free)

**Cost: ~$40**

### Mid-Range Option

- 2.0mm board thickness
- HASL (leaded/lead-free)

**Cost: ~$100**

### Best Configuration
*Recommended*

- 2.0mm thickness
- Black color (or your preference)
- ENIG finish

**Cost: ~$150**

### Important Notes

If you choose the cheapest option for experimentation, you'll need to make adjustments to ensure proper USB port fit. The 1.6mm thickness may cause the board to slip out of USB ports. Solutions include:

- Adding masking tape layers to increase thickness
- 3D printing a spacer to reach 2.0-2.2mm height

A 2.0mm thickness ensures the board stays securely in USB ports.

**Experimental Idea:** You could order 1.0mm thick boards (same cost as 1.6mm) and glue them together to achieve 2.0mm thickness. I have not personally tested this yet.