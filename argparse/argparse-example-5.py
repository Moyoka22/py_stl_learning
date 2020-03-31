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

     
    args = parser.parse_known_args() # * Will consume recognised arguments and leave th rest alone ; Return is a tuple of a Namespace and a list of remaining tokens
    return args

def main(args):
    p = pprint.PrettyPrinter(indent=4)
    p.pprint(vars(args[0]))
    print(args[1]) 


if __name__ == '__main__':
    args = parse_args()
    main(args)
