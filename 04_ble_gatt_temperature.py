import machine
import time

uart = machine.UART(0, baudrate=115200)

i2c = machine.I2C(1, sda=machine.Pin(14), scl=machine.Pin(15), freq=100000)
addr = 0x48
i2c.writeto_mem(addr, 0x01, b'\x60')

# INSERT HANDLE BELOW
gatt_handle = "1002"

uart.write("$$$")
time.sleep(1)

while True:
    data = i2c.readfrom_mem(addr, 0x00, 2)
    value = (data[0] << 8) | data[1]
    value = value >> 4

    if value > 2047:
        value = value - 4096

    temp = value * 0.0625
    t100 = int(temp * 100)

    temp_hex = "{:02X}{:02X}".format(
        t100 & 0xFF,
        (t100 >> 8) & 0xFF
    )

    print("{:.2f} °C".format(temp) + " - HEX:", temp_hex)

    uart.write("SHW," + gatt_handle + "," + temp_hex + "\r")
    time.sleep(3)
