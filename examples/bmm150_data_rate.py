# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_bmm150 import bmm150

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
bmm = bmm150.BMM150(i2c)

bmm.data_rate = bmm150.RATE_2HZ

while True:
    for data_rate in bmm150.data_rate_values:
        print("Current Data rate setting: ", bmm.data_rate)
        for _ in range(10):
            magx, magy, magz = bmm.magnetic
            print("x:{:.2f}T, y:{:.2f}T, z:{:.2f}T".format(magx, magy, magz))
            print()
            time.sleep(0.5)
        bmm.data_rate = data_rate
