#!/usr/bin/env python3
#
from pprint import pprint
import argparse

parser = argparse.ArgumentParser(description="help")
parser.add_argument('--input', nargs="+")
args = parser.parse_args()

pprint("#")
pprint(args)

pprint("#")
pprint(type(args))

pprint("#")
pprint(args.input)

pprint("#")
pprint(type(args.input))
