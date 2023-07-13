#!/usr/bin/python3
"""
read-file print the file content

   
"""
def read_file(filename=""):
    """ 
    Args:
        filename (path): file path

    """
    with open(filename, 'r',encoding='UTF-8') as f:
        print(f.read(), end='')

