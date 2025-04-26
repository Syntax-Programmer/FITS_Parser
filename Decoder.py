from astropy.io import fits
import pyfiglet
import pandas as pd
import os
import csv
import time

TO_PARSE_LIST_PATH = "ToParse.csv"
filepath_sep = "\\" if os.name == "nt" else "/"


def ClearScreen() -> None:
    if os.name == "nt":  # windows system.
        os.system("cls")
    else:  # unix based system.
        os.system("clear")


def PrintFITSIntoTxtInterface() -> None:
    ClearScreen()
    print("\033[3;34m+-------------+\033[0m")
    print("Parse FITS file")
    print("\033[3;34m+-------------+\033[0m\n")


def ClearDir(dir_path: str) -> None:
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


def DecodeFITS(fits_filepath: str, target_dir_name: str, metadata=False) -> None:
    start_time = time.perf_counter()

    if not os.path.isdir(target_dir_name):
        # Making the directory if not exist that will hold all the csv files.
        os.mkdir(target_dir_name)
    else:
        # Cleaning the dir, so that any irrelevant/outdated files not remain in the dir.
        ClearDir(target_dir_name)

    try:
        with (
            fits.open(fits_filepath, memmap=True) as hdu_list,
        ):
            # Go through each HDU and print contents
            for hdu in hdu_list:
                file_path = (
                    f"{target_dir_name}{filepath_sep}{target_dir_name}_{hdu.name}"
                )
                with open(
                    f"{file_path}.csv",
                    "w",
                    newline="",
                ) as target:
                    if hdu.data is not None:
                        if metadata:
                            metadata_file = open(f"{file_path}_METADATA.txt", "w")
                            metadata_file.write(f"{repr(hdu.header)}\n\n")
                            metadata_file.close()
                        df = pd.DataFrame(hdu.data.tolist())
                        df.to_csv(target, index=False, header=(target.tell() == 0))
    except OSError as e:
        print(f"\nERROR: {e}\n")
    print(f"Operation Completed in: {time.perf_counter() - start_time} seconds.")


def ParseFITSIntoTxt() -> None:
    PrintFITSIntoTxtInterface()

    try:
        to_parse_list = open(TO_PARSE_LIST_PATH, "r")
    except OSError:
        print("\033[3;31m+-----------------------------+\033[0m")
        print(
            f"ERROR: The file {TO_PARSE_LIST_PATH} doesn't exist. File is needed(even empty) for the parsing to work."
        )
        print("\033[3;31m+-----------------------------+\033[0m\n")
        input("Press Enter to Continue: ")
        return
    reader = csv.reader(to_parse_list, delimiter=",")

    for file in reader:
        fits_filepath, metadata, *_ = file
        target_dir_name = fits_filepath[:-5]

        fits_filepath = fits_filepath.strip()
        metadata = (
            # Just a "MAKE It WORK" solution to account for both types of conditions we can encounter.
            True if metadata.strip().lower() == "metadata=true" else False
        )

        print(
            f"\nStarted parsing '{fits_filepath}' and output will be sent to '{target_dir_name}' directory."
        )
        DecodeFITS(fits_filepath, target_dir_name, metadata=metadata)
        print(
            f"Ended parsing '{fits_filepath}' and output will has been sent to '{target_dir_name}' directory.\n"
        )
    to_parse_list.close()
    input("Press Enter to Continue: ")


def PrintMainInterface() -> None:
    ClearScreen()
    print(
        f"\033[1;34m{pyfiglet.figlet_format('Welcome to the\n', font='banner3', width=1000)}\n{pyfiglet.figlet_format('FITS   Data   Parser', font='banner3', width=1000)}\033[0m"
    )
    print("\n\033[3;34m+--------------------+\033[0m")
    print("1. Parse FITS")
    print("\033[3;34m+--------------------+\033[0m")
    print("2. Plot Data")
    print("\033[3;34m+--------------------+\033[0m")
    print("3. Exit")
    print("\033[3;34m+--------------------+\033[0m\n")


def main() -> None:
    while True:
        PrintMainInterface()
        choice = input("Enter your choice to continue: ")
        if choice == "1":
            ParseFITSIntoTxt()
        elif choice == "2":
            pass
        elif choice == "3":
            ClearScreen()
            print("\033[3;34m+-----------------------------+\033[0m")
            print("Exiting the program, Thank You!")
            print("\033[3;34m+-----------------------------+\033[0m\n")
            exit(0)


if __name__ == "__main__":
    main()
