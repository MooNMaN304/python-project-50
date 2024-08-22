#!/usr/bin/env python3
from gendiff import gen_diff, parse_args

def main():
    args = parse_args()
    different = gen_diff(args.first_file, args.second_file)
    print(different)


if __name__ == '__main__':
    main()
