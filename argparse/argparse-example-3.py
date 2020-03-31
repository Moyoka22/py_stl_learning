# -*- coding: utf-8 -*-
"""Further examples with subparsers"""
import argparse
import pprint

def subcommand1(args):
    print('Subcommand 1 executed.')

def subcommand2(args):
    print('Subcommand 2 executed.')

def parse_args():
    parser = argparse.ArgumentParser(usage=
    """py argparse-example-1.py -z hello -f meh -b H -q -x 2 3 4 -i 3 -i 4 -i 5""")
    parser.add_argument('--version',action='version',version='%(prog)s v0.1') # When using the version action the version keyword must be supplied
    subparsers = parser.add_subparsers(title='subcommand1')

    # 
    parser_a = subparsers.add_parser('subcommand1',help='Subparser a') 
    parser_a.add_argument('foo')
    parser_a.add_argument('-b','--bar')
    parser_a.set_defaults(func=subcommand1) # By setting a func object default here the correct handler can be called later

    # py .\argparse-example-2.py subcommand2 -x a
    parser_b = subparsers.add_parser('subcommand2',help='Subparser b')
    parser_b.add_argument('qux')
    parser_b.set_defaults(func=subcommand2) # * Sets arguments without them being specified on the command line


     
    args = parser.parse_args()
    return args

def main(args):
    args.func(args) # Here the appropriate handler function is called for the subcommand


if __name__ == '__main__':
    args = parse_args()
    main(args)
