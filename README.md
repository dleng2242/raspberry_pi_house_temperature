
# Python Raspberry Pi House Temperature Sensor app

This repo contains code for my home temperature sensor app that reads
from a BMP180 temperature chip connected to a Raspberry Pi Model 1 B. 

I wrote this code a while back and thought I'd tidy it up and add it here. 


## Quick start

I used python 3.10 and developed the code on my laptop in VS code, and 
then pulled the code onto the Raspberry Pi to run it.

Some packages will only install on the Raspberry Pi OS, and others are only
needed for development, so there are two environment files: `env_dev.yml`
for development on my PC, and `env_prd.yml` for the Raspberry Pi. 

Use `conda env create -f env_prd_.yml` to recreate the environment.
Or you can use `conda env update -f env_prd.yml --prune` to just
update an already created environment. 

The Raspberry Pi was connected to my home network using an ethernet cable
directly into the router as its an old model without wifi. 

Use `pinout` to get the Raspberry Pi pin layout, and then connect the BMP180
sensor as follows: 

BMP180 chip
* VIN - 3v3 into pin 2 (top left)
* GND - ground into pin 6 (third right)
* SCL - clock into pin 5 (third left)
* SDA - data into pin 3 (second left)

LED
* Signal from pin 7 (fourth left) via resistor into ground

To run the code use `python3 src/main.py -v` from the project root. 
It should print out the sensor readings, and append them to file. 



