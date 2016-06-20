#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

"""Main module."""

import argparse


def main():
    args = parse_args()
    the_file = args.filepath[0]
    with open(the_file) as f:
        print(f.read())


def parse_args():
    parser = argparse.ArgumentParser(
        description='{{ cookiecutter.package_description }}')
    parser.add_argument('filepath', metavar='inputfile', type=str, nargs=1,
                        help='File to read and output content.')
    return parser.parse_args()


if __name__ == '__main__':
    main()
