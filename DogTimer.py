#
# **BovosCarpentryCODE**
#
from rpi_lcd import LCD
from signal import signal, SIGTERM, SIGHUP
from gpiozero import Button
from datetime import datetime
from time import sleep
import time
#
#
lcd = LCD()
button = Button(17)
#
#
def safe_exit(signum, frame):
    exit(1)
#
#
while True:
    button.wait_for_press()
    lcd.clear()
    lcd.text("*  DATE & TIME *", 1)
    lcd.text("*   UPDATING   *", 2)
    sleep(3)
    lcd.text("*  DATE & TIME *", 1)
    lcd.text("*    UPDATED   *", 2)
    sleep(2)
    lcd.text("*MILLIE WAS FED*", 1)
    lcd.text(time.strftime("*%d %b %I:%M%p*"), 2)
    sleep(2)
    continue
#
#