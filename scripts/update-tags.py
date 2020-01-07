#!/usr/bin/python3

import datetime
import fileinput
import glob
import os
from os.path import isfile, join
import re
import subprocess
import sys

commit = subprocess.getoutput("git rev-parse HEAD").split()[0]
tstamp = '{:%Y%m%d:%H.%M}'.format(datetime.datetime.utcnow())

def update_tags(fname):
  with fileinput.input(fname, inplace=True, backup=".bak") as fd:
      cpat = re.compile(r'^(\s+)Value:\s+"COMMIT:')
      tpat = re.compile(r'^(\s+)Value:\s+"TIMESTAMP:')

      for line in fd:
          cmatch = cpat.match(line)
          tmatch = tpat.match(line)
          if cmatch:
              nval = cmatch.group(1)+'Value: "COMMIT: '+commit+'"\n'
              sys.stdout.write(nval)
          elif tmatch:
              nval = tmatch.group(1)+'Value: "TIMESTAMP: '+tstamp+'"\n'
              sys.stdout.write(nval)
          else:
              sys.stdout.write(line)


for tmpl in glob.glob("templates/*.yaml"):
    print("Updating "+tmpl)
    update_tags(tmpl)

