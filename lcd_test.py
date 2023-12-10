#! /usr/bin/env python3

import time
from liquidcrystal_i2c import LCD

LCD_ADDRESS=0x27
LCD_BUS=0
LCD_COLS=20
LCD_ROWS=4

lcd = LCD(bus=LCD_BUS, addr=LCD_ADDRESS, cols=LCD_COLS, rows=LCD_ROWS)
lcd.clear()
lcd.home()
lcd.setCursor(3,1)

lcd.print("Hello, world!")
time.sleep(1)
lcd.noBacklight()
time.sleep(1)
lcd.backlight()

