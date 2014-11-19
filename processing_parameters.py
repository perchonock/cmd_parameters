__author__ = 'adm'

import argparse
import sys
a = sys.argv
parser = argparse.ArgumentParser()

parser.add_argument('-case')
parser.add_argument('nm')
b = parser.parse_args(['rnm', "-case", "lower"])

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

args = parser.parse_args(['1', '2', '3', '4'])

print(args)

