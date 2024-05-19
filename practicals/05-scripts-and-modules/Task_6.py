#!/usr/bin/env python3

import os
import sys
import shutil


def copy(file_name):
    current_dir = os.getcwd()
    src_path = os.path.join(current_dir, file_name)
    dest_path = os.path.join(current_dir, "copy_of_" + file_name)
    shutil.copy(src_path, dest_path)


if __name__ == "__main__":
    try:
        file = sys.argv[1]
        copy(file)
    except IndexError:
        print('No arguments given')
