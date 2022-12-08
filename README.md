
# Python Raspberry Pi House Temperature Sensor app

This repo contains code for my home temperature sensor app that reads
from a BMP180 temperature chip connected to a Raspberry Pi Model 1 B. 

I wrote this code a while back and thought I'd tidy it up and add it here. 


## Quick start

I used python 3.10 and developed the code on my laptop in VS code, and 
then pulled the code onto the Raspberry Pi to run it.

The Raspberry Pi was tricky to manage environments on. First, the highest
python version available on the Pi was only 3.4.3, second it was too 
old for miniconda to be install, and third some packages
will only install on the Raspberry Pi OS and not on windows, with some 
packages only needed for development. 
To resolve all this I created two environment 
files: `env_dev.yml` for development on my PC inside a conda environment,
and `requirements_prd.txt` for the Raspberry Pi. 


Use `conda env create -f env_dev.yml` to recreate the environment.
Or you can use `conda env update -f env_dev.yml --prune` to just
update an already created environment. 

Use `pip install -r requirements_prd.txt` to install the requirements on
the Raspberry Pi. 

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

Here is mine:

![my RP setup](https://raw.githubusercontent.com/dleng2242/raspberry_pi_house_temperature/main/images/rp_setup.png)

