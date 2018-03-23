
## Scraper
Multiclass and binary have overlapping Tweets (multiclass is a subset of binary). Not all Tweets
are available because some accounts were suspended in the meantime. In total, our scraper collected
105914 of them.

## SyntaxNet
SyntaxNet is installed [via Docker](
https://github.com/tensorflow/models/blob/master/research/syntaxnet/g3doc/CLOUD.md), find sh
convenience scripts in the `syntaxnet` directory.

The file `wrapper.py` contains a script adapted from
[nardeas/tensorflow-syntaxnet](https://github.com/nardeas/tensorflow-syntaxnet). It uses models
which come with the default Docker image for DRAGNN
(`/opt/tensorflow/syntaxnet/examples/dragnn/data/`).

