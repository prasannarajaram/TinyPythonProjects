#! /usr/bin/python3
# Purpose: Say hello
'''Docstring'''
# import pdb
import argparse


def get_args():
    '''Getting arguments from command line'''
    parser = argparse.ArgumentParser(description='Say Hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    '''Hello World program'''
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
