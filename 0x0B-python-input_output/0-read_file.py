#!/usr/bin/python3


def read_file(filename=""):
    """ read-file print the file content
    Args:
        filename (path): file path

    """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
