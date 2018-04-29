import os
import json
import sys
from dragnn.wrapper import SyntaxNet
import logging

DATA = '/data'
sn = SyntaxNet(lang="English", model_dir="/usr/local/tfmodels", logging=False)

out_fpath = os.path.join(DATA, 'tweets_sn_parsed.json')
in_fpath = os.path.join(DATA, 'tweets_normalized.txt')
if os.path.exists(out_fpath):
  print "File %s exists, won't overwrite" % out_fpath
  sys.exit(1)

with open(out_fpath, 'w') as f_out, open(in_fpath) as f_in:
  parsed = []
  for i, tweet in enumerate(f_in):
    as_json = sn.parse(tweet.strip())
    as_json['index'] = i
    parsed.append(as_json)
    if i % 5000 == 0:
      logging.info("Done parsing %d", i)

  json.dump(parsed, f_out, indent=2)
