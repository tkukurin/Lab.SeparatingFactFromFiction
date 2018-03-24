import os
import json
import sys
from dragnn.wrapper import SyntaxNet

DATA = '/data'
sn = SyntaxNet(lang="English", model_dir="/usr/local/tfmodels", logging=False)
start = 0

with open(os.path.join(DATA, 'parsed_start_{}.json'.format(start)), 'w') as f_out, \
    open(os.path.join(DATA, 'tweets_normalized.txt')) as f_in:
  f_out.write("[")
  for i, tweet in enumerate(f_in):
    as_json = sn.parse(tweet.strip()) if len(tweet.strip()) > 0 else {}
    as_json['index'] = i

    json.dump(as_json, f_out, indent=2)
    f_out.write(",")
  f_out.write("]")
