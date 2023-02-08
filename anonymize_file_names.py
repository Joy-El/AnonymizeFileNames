#!/usr/bin/env python3
"""Anonymize File Names based on a provided original -> anonymized mappings CSV.

Example CSV line: 2022-03-15_S_Holmes.OBJ,Scan_57831864.OBJ
"""


import argparse  # help menu and argument processing
import csv  # parse mapping CSV file
import os  # output folder creation
import shutil  # copying the files


def get_args():
    """Return parsed command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Anonymize file names based on provided mappings CSV"
        )

    parser.add_argument('-m', '--mappings',
                        metavar='CSV',
                        help="Provide the path to the mappings CSV",
                        default="mappings.csv",
                        type=str)
    parser.add_argument('-f', '--files',
                        metavar="FOLDER",
                        help="Provide the path to the folder with the files to anonymize.",
                        default="to_anonymize",
                        type=str)
    parser.add_argument('-o', '--output',
                        metavar="FOLDER",
                        help="Provide the path to store anonymized output files.",
                        default="anonymized",
                        type=str)
    return(parser.parse_args())


def make_subdirectories(path):
    """Create subdirectories for a path."""
    os.mkdir(os.path.split(path)[0])


def anonymize_files(args):
    """Anonymize file names."""
    # Make output folder
    try:
        os.mkdir(args.output)
    except FileExistsError as e:
        print(f"\nThe folder {args.output} already exists.")
        print("Specify an output folder that doesn't exist yet.\n")
        raise(e)

    # Parse through mappings folder and copy files to new named location
    with open(args.mappings, mode='r') as input_file:
        csv_file = csv.reader(input_file)
        next(csv_file)  # skip header line
        for mapping in csv_file:
            try:
                source = os.path.join(args.files, mapping[0])
                anonymized = os.path.join(args.output, mapping[1])
                try:
                    shutil.copy(source, anonymized)
                except FileNotFoundError:  # subfolder is missing
                    make_subdirectories(anonymized)
                    # retry copy:
                    shutil.copy(source, anonymized)
            except IndexError:
                if len(mapping) != 0:
                    print(f"Unable to annonymize line: {str(mapping)}")


if __name__ == '__main__':
    anonymize_files(get_args())
