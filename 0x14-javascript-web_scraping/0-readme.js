#!/usr/bin/node
import sys

def read_and_print_file(file_path):
    """
    Reads and prints the content of a file.

    Parameters:
    file_path (str): The path to the file to read.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
    else:
        file_path = sys.argv[1]
        read_and_print_file(file_path)

