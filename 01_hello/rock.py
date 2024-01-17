#!/usr/bin/env python3
'''Rock the casbah'''

import argparse
# import os
# import sys


def get_args():
    '''Get command line arguments'''

    parser = argparse.ArgumentParser(
        description='Rock the casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('positional',
                        metavar='str',
                        help='A pos arg')

    parser.add_argument('-a',
                        '--arg',
                        help='A named str arg',
                        metavar='str',
                        type='str',
                        default='')

    parser.add_argument('-i',
                        '--int',
                        help='A named int arg',
                        metavar='int',
                        type='int',
                        default='')

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-o',
                        '--on',
                        help='A bool flag',
                        action='store_true')

    return parser.parse_args()


def main():
    '''Make Jazz noise here'''

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f'str_arg =  "{str_arg}"')
    print(f'int_arg =  "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    print(f'pos_arg =  "{pos_arg}"')


if __name__ == '__main__':
    main()
