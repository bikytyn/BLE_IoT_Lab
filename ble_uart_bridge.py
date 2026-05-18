import machine
import time

uart = machine.UART(0, baudrate=115200)

print("cmd = Enter command mode")
print("data = Enter data mode")
print()

while True:
    text = input("> ")

    if text == "cmd":
        uart.write("$$$")
        time.sleep(0.5)

    elif text == "data":
        uart.write("---\r")
        time.sleep(0.5)

    else:
        uart.write(text + "\r")
        time.sleep(0.5)

    while uart.any():
        response = uart.read()
        print(response.decode("utf-8", "ignore"), end="")

    print()
