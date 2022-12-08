"""
src/main.py

Main entry module for getting sensor readings. 

"""

import argparse
import datetime
import os

from data_io import append_readings_local_csv
from sensor import get_BMP180_reading


def main(verbose=True):
    time = datetime.datetime.now()
    temp, pressure, altitude = get_BMP180_reading()
    if verbose:
        print(f"Datetime:    {time}")
        print(f"Temperature: {temp:.2f} C")
        print(f"Pressure:    {pressure:.2f} hPa")
        print(f"Altitude:    {altitude:.2f} m")

    # save datetime, and just temp and pressure
    readings = [time, temp, pressure]
    file = os.path.join("data", "output_reading.csv")
    append_readings_local_csv(readings, file, verbose=False)


if __name__ == "__main__":

    # Construct the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--verbose",
        action='count', 
        default=0,
        help="Make output verbose using -v",
    )
    args = vars(parser.parse_args())

    verbose = False
    if args["verbose"] > 0:
        verbose = True

    main(verbose)
