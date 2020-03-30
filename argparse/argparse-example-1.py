# -*- coding: utf-8 -*-

import argparse
import pprint

def parse_args():
    parser = argparse.ArgumentParser(usage=
    """py argparse-example-1.py -z hello -f meh -b H -q -x 2 3 4 -i 3 -i 4 -i 5""")
    parser.add_argument('--version',action='version',version='%(prog)s v0.1') # When using the version action the version keyword must be supplied
    parser.add_argument('-f','--foo',help='foo variable') # Help keyword provides help 
    parser.add_argument('-b','--bar',choices=['H','M','L']) # Choices keyword to restrict to several choices
    parser.add_argument('-z','--baz',required=True,dest='bzz') # Required keyword to force provision of an argument. Destination keyword changes the name of the variable in the namespace object
    parser.add_argument('-q','--qux',action='store_const',const=(lambda x : x**2)) # When using store_const action the constant keyword must be supplied, const can be anything
    parser.add_argument('-c','--corge',type=int,default=12) # Default values for optional types with default. Type restricts values
    parser.add_argument('-x','--quux',action='extend',nargs='+') # Extend action allows supplying multiple arguments into one collection, nargs + means at least one must be supplied
    parser.add_argument('-i','--blip',action='append',nargs='?') # Append will allow supplying of multiple arguments and append them to a collection. Unlike extend it will not automatically consume additional values without resupplying the flag
    parser.add_argument('-s','--suppressed',default=argparse.SUPPRESS) # If not supplied this will not be present in the namespace
    # parser.add_argument('-a','-additional', namespace=some_namespace) # * Can add arguments to an already existing namespace 
    args = parser.parse_args()
    return args

def main(args):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(vars(args))

if __name__ == '__main__':
    args = parse_args()
    main(args)
