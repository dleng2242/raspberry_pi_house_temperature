"""
src/sensor.py

Module for getting sensor readings. 

"""
import time
import datetime
import RPi.GPIO as GPIO

from Adafruit_BMP085 import BMP085


def get_BMP180_reading():
    """
    Get reading from the BMP180 temperature, pressure, and altitude chip on 
    the Raspberry Pi. 
    
    Also flashed LED from pin 7 when reading taken. 
    I do not think the altitude works?

    Assumes components connected as follows:
        BMP180 chip
        VIN - 3v3 into pin 2 (top left)
        GND - ground into pin 6 (third right)
        SCL - clock into pin 5 (third left)
        SDA - data into pin 3 (second left)

        LED
        Signal from pin 7 (fourth left)
        via resistor into ground

    Use `pinout` to get the PR pin layout.

    Returns: 
    Temperature (C), pressure (hPa/millibar), and altitude. 

    """

    # Initialise the BMP085 and use STANDARD mode (default value)
    bmp = BMP085(0x77)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)

    try:
        # LED on (pin 7)
        GPIO.output(7, True)
    
        temp = bmp.readTemperature()
        pressure = bmp.readPressure()
        altitude = bmp.readAltitude()

        # convert pressure from Pascals to millibar
        pressure = pressure / 100.0

        # LED off
        time.sleep(1)
        GPIO.output(7, False)

    finally:
        GPIO.cleanup()
        # if fails, just return None
        temp, pressure, altitude = (None,)*3
    
    return temp, pressure, altitude


def main(verbose=True):
    time = datetime.datetime.now()
    temp, pressure, altitude = get_BMP180_reading()
    if verbose:
        print(f"Datetime:    {time}")
        print(f"Temperature: {temp[0]:.2f} C")
        print(f"Pressure:    {pressure[1]:.2f} hPa")
        print(f"Altitude:    {altitude[2]:.2f} m")


if __name__ == "__main__":
    main()
