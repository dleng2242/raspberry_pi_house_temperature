"""
src/data_io.py

Module for getting data in and out of the app. 

"""

import datetime
import os


def append_readings_local_csv(row, file, verbose=False):

    # first convert row elements to strings if not already
    row = [str(val) for val in row]

    # concatenate row into one string
    string_results = ",".join(row) + "\n"

    f_dir, f_name = os.path.split(file)
    if not os.path.exists(f_dir):
        os.makedirs(f_dir, exist_ok=True)
        print(f"Directory created at {f_dir}")
    
    with open(file, "a") as f:
        f.write(string_results)
   
    if verbose:
        print(f"Data saved to file {file}")
   

def main(verbose=True):
    time = datetime.datetime.now()
    if verbose:
        print(f"Data IO module ran as script {time}")
    # maybe add status of DB?


if __name__ == "__main__":
    main()
