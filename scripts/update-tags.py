#!/usr/bin/python3

# Update the metadata tags for all the templates under the `templates`
# directory. This includes the _current_ git hash, and a timestamp.
# The use of the hash is ugly (as in practice it will always lag the
# real commit hash) but in conjunction with the timestamp is simplest
# method of tying a given CFN stack to a version.

import datetime
import fileinput
import glob
import re
import subprocess
import sys

# Use same ISO8601 format as Ansible. See https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/facts/system/date_time.py
tstamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
commit = subprocess.getoutput("git rev-parse HEAD").split()[0]

def update_tags(fname):
  with fileinput.input(fname, inplace=True) as fd:
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

