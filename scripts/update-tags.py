#!/usr/bin/python3

import datetime
import fileinput
import re
import subprocess
import sys

TEMPLATE = 'templates/quickstart-vpc-for-atlassian-services.yaml'

commit = subprocess.getoutput("git rev-parse HEAD").split()[0]
tstamp = '{:%Y%m%d:%H.%M}'.format(datetime.datetime.utcnow())

with fileinput.input(TEMPLATE, inplace=True, backup=".bak") as fd:
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

