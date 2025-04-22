from astropy.io import fits
import numpy as np
import pyfiglet
import os


def ClearScreen() -> None:
    if os.name == "nt":  # windows system.
        os.system("cls")
    else:  # unix based system.
        os.system("clear")


def PrintFITSIntoTxtInterface() -> None:
    ClearScreen()
    print("\033[3;34m+-------------+\033[0m")
    print("Parse FITS file")
    print("\033[3;34m+-------------+\033[0m")


def ConvertNumpyLiteralToVal(val):
    if isinstance(val, np.generic):  # scalar numpy types like np.int32, np.float64
        return val.item()
    elif isinstance(val, np.ndarray):  # numpy arrays (e.g. array([...]))
        return val.tolist()
    return val


def ParseFITSIntoTxt() -> None:
    PrintFITSIntoTxtInterface()
    fits_filepath = input("\nEnter the filepath of the FITS file: ")
    target_filepath = input("\nEnter the filepath of the target file: ")

    try:
        with open(target_filepath, "w") as target:
            with fits.open(fits_filepath) as hdu_list:
                # Print general FITS structure
                hdu_list.info()

                # Go through each HDU and print contents
                for i, hdu in enumerate(hdu_list):
                    target.write(
                        "\n\n\n+---++---++---++---++---++---++---++---++---++---++---+"
                    )
                    target.write(
                        f"\n\n+----------------- HDU {i} ({hdu.name}) -----------------+"
                    )
                    # Show header
                    target.write("\n\n+========+ Header: +========+\n")
                    target.write(repr(hdu.header))

                    # If it contains data, show it
                    if hdu.data is not None:
                        target.write("\n\n+========+ Data in the HDU: +========+\n")
                        for row in hdu.data:
                            target.write(
                                f"{[ConvertNumpyLiteralToVal(col) for col in row]}\n"
                            )
                    else:
                        target.write(
                            "\n\n+========+ No data found in the HDU: +========+\n"
                        )
                    target.write(
                        "\n\n\n+---++---++---++---++---++---++---++---++---++---++---+"
                    )
    except OSError as e:
        print(f"\nError: {e}\n")
    input("Press Enter to Continue: ")


def PrintMainInterface() -> None:
    ClearScreen()
    print(
        f"\033[1;34m{pyfiglet.figlet_format('Welcome to the\n', font='banner3', width=1000)}\n{pyfiglet.figlet_format('FITS   Data   Parser', font='banner3', width=1000)}\033[0m"
    )
    print("\n\033[3;34m---------------------+\033[0m")
    print("1. Parse FITS")
    print("\033[3;34m---------------------+\033[0m")
    print("2. Exit")
    print("\033[3;34m+--------------------+\033[0m\n")


def main() -> None:
    while True:
        PrintMainInterface()
        choice = input("Enter your choice to continue: ")
        if choice == "1":
            ParseFITSIntoTxt()
        elif choice == "2":
            ClearScreen()
            print("\033[3;34m+-----------------------------+\033[0m")
            print("Exiting the program, Thank You!")
            print("\033[3;34m+-----------------------------+\033[0m")
            exit(0)


if __name__ == "__main__":
    main()
