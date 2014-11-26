__author__ = 'adm'

import argparse
import sys

a = sys.argv
parser = argparse.ArgumentParser()
parser.add_argument('-num', type=int, required=True)
parser.add_argument('-stro', type=str)
parser.add_argument('-smile', action='store_true')
parser.add_argument('pyfile', nargs='?')
#args = parser.parse_args("-num 5 -smile -stro qq".split())
args = parser.parse_args(a)
print(args.pyfile)
if args.stro != None:
    print((args.stro+"\n")*args.num, end='')
else:
    print(args.num)
if args.smile:
    print(":)")


