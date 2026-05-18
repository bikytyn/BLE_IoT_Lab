import machine
import neopixel
import time

uart = machine.UART(0, baudrate=115200)
uart.write("---\r")
time.sleep(0.5)

np = neopixel.NeoPixel(machine.Pin(16), 3, bpp=4)

intensity = 10

r = 0
g = 0
b = 0
w = 0

def update_leds():

    rr = r * intensity // 255
    gg = g * intensity // 255
    bb = b * intensity // 255
    ww = w * intensity // 255

    for i in range(3):
        np[i] = (rr, gg, bb, ww)

    np.write()


while True:

    if uart.any():

        command = uart.read().decode().strip().lower()

        print(command)

        if command == "off":
            r = 0
            g = 0
            b = 0
            w = 0

        elif command == "red":
            r = 255
            g = 0
            b = 0
            w = 0

        elif command == "green":
            r = 0
            g = 255
            b = 0
            w = 0

        elif command == "blue":
            r = 0
            g = 0
            b = 255
            w = 0

        elif command == "white":
            r = 0
            g = 0
            b = 0
            w = 255

        elif command == "yellow":
            r = 255
            g = 255
            b = 0
            w = 0

        elif command == "cyan":
            r = 0
            g = 255
            b = 255
            w = 0

        elif command == "magenta":
            r = 255
            g = 0
            b = 255
            w = 0

        elif command.startswith("intensity="):

            intensity = int(command.replace("intensity=", ""))

            if intensity < 0:
                intensity = 0

            if intensity > 255:
                intensity = 255

        elif command == "gpio_on":

            uart.write("$$$")
            time.sleep(0.5)

            uart.write("|O,0002,0002\r")
            time.sleep(0.5)

            uart.write("---\r")
            time.sleep(0.5)

        elif command == "gpio_off":

            uart.write("$$$")
            time.sleep(0.5)

            uart.write("|O,0002,0000\r")
            time.sleep(0.5)

            uart.write("---\r")
            time.sleep(0.5)

        update_leds()

    time.sleep(0.1)
