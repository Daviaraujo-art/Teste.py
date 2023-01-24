import sys
import os
import constants
from my_structure import NumberStorage


def get_filename_arg():
    args = sys.argv
    if len(args) < constants.MIN_ARGS:
        raise Exception("You must pass at least one argument")
    if args[1].endswith(".txt") is False:
        raise Exception("The file argument must end with .txt")
    # TODO: validate if the file, actually exists.
    return args[1]


def run():
    file_name = get_filename_arg()
    storage = NumberStorage()
    with open(file_name, "r") as input_file:
        for line in input_file:
            try:
                number = int(line)
            except Exception as e:
                print(e)
                # raise Exception("...")
                continue
            storage.add_number(number)

    absolute_path = os.path.dirname(__file__)
    file_path = absolute_path+"/"+constants.OUTPUT_FILE_NAME
    with open(file_path, "w") as output_file:
        for number, status in storage.get_numbers().items():
            output_file.write(status + ": " + str(number) + "\n")
            print(number, status)