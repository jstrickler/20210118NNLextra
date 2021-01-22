#!/usr/bin/env python
import sys
from glob import glob
import fileinput

files = glob(sys.argv[1])

for line in fileinput.input(files):  # <1>
    if 'bird' in line:
        print('{}: {}'.format(fileinput.filename(), line), end=' ')  # <2>
