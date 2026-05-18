import machine
import time

uart = machine.UART(0, baudrate=115200)

uart.write("---\r")
time.sleep(0.5)
uart.write("$$$")
time.sleep(1)

print("Factory Reset")
uart.write("SF,1\r")
time.sleep(1)

print("Reboot")
uart.write("R,1\r")
time.sleep(3)

uart.write("---\r")
time.sleep(0.5)
uart.write("$$$")
time.sleep(1)

print("Status LED Initialization")
uart.write("SR,0001\r")
time.sleep(0.5)

print("Reboot")
uart.write("R,1\r")
time.sleep(3)

uart.write("---\r")
time.sleep(0.5)
uart.write("$$$")
time.sleep(1)

print("GPIO LED Initialization")
uart.write("|O,0002,0000\r")
time.sleep(0.5)

uart.write("---\r")
time.sleep(0.5)

print("Done")
