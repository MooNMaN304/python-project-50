#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description='''Compares two configuration
    files and shows a difference.''')
    parser.add_argument('first_file', help='path to the first file')
    parser.add_argument('second_file', help='path to the second file')


if __name__ == "__main__":
    main()
