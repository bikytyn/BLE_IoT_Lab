import machine
import time
import sys
import select

uart = machine.UART(0, baudrate=115200)

print("cmd  = Enter command mode")
print("data = Enter data mode")
print()

while True:

    # BLE -> Thonny
    if uart.any():
        line = uart.readline()

        if line:
            text = line.decode("utf-8", "ignore").strip()

            if text != "":
                print()
                print(text, end="")

    # Thonny -> BLE
    if select.select([sys.stdin], [], [], 0)[0]:
        command = sys.stdin.readline().strip()

        if command == "cmd":
            uart.write("$$$")

        elif command == "data":
            uart.write("---\r")

        else:
            uart.write(command + "\r")

    time.sleep(0.02)
