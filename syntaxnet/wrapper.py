import os
import json
import sys
from dragnn.wrapper import SyntaxNet

DATA = '/data'
sn = SyntaxNet(lang="English", model_dir="/usr/local/tfmodels", logging=False)

with open(os.path.join(DATA, 'tweets_sn_parsed.json'), 'w') as f_out, \
    open(os.path.join(DATA, 'tweets-normalized-v2.txt')) as f_in:
  # f_out.write("[")

  parsed = []
  for i, tweet in enumerate(f_in):
    as_json = sn.parse(tweet.strip())
    as_json['index'] = i
    parsed.append(as_json)
    if i % 5000 == 0:
      print("Done parsing:", i)

  json.dump(parsed, f_out, indent=2)

    # f_out.write(",")
  # f_out.write("]")