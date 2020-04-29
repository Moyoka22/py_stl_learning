# -*- coding: utf-8 -*-
"""Examples with argument groups"""
import argparse
import pprint


def parse_args():
    parser = argparse.ArgumentParser(usage=
    """py argparse-example-1.py -z hello -f meh -b H -q -x 2 3 4 -i 3 -i 4 -i 5""")
    parser.add_argument('--version',action='version',version='%(prog)s v0.1') # When using the version action the version keyword must be supplied
    group_one = parser.add_argument_group(title='group one',description='An argument group')
    group_one.add_argument('-f','--foo')
    group_one.add_argument('-b','--bar')

    """py argparse-example-4.py -z a -q b""" # * Fails because -z and -q cannot be applied together
    group_two = parser.add_mutually_exclusive_group()
    group_two.add_argument('-z','--baz')
    group_two.add_argument('-q','--qux')

     
    args = parser.parse_args()
    return args

def main(args):
    p = pprint.PrettyPrinter(indent=4)
    p.pprint(vars(args))


if __name__ == '__main__':
    args = parse_args()
    main(args)
