import sys
import fileinput
from argparse import ArgumentParser

parser = ArgumentParser(description="Faux Grep")

parser.add_argument('-i', dest="ignorecase", action="store_true", help="Ignore case")
parser.add_argument('pattern', help="pattern to find")
parser.add_argument('files', nargs='*', help="files to search")

args = parser.parse_args()

pattern = args.pattern
if args.ignorecase:
    pattern = pattern.lower()

for real_line in fileinput.input(args.files):
    line = real_line
    if args.ignorecase:
        line = real_line.lower()
    if pattern in line:
        print(real_line.rstrip())

