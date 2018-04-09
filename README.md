
## Scraper
Multiclass and binary have overlapping Tweets (multiclass is a subset of binary). Not all Tweets
are available because some accounts were suspended in the meantime. In total, our scraper collected
119,136 of them.


## SyntaxNet
SyntaxNet is installed [via Docker](
https://github.com/tensorflow/models/blob/master/research/syntaxnet/g3doc/CLOUD.md), find sh
convenience scripts in the `syntaxnet` directory.

The file `wrapper.py` is to be run from within a docker container obtained from
[nardeas/tensorflow-syntaxnet](https://github.com/nardeas/tensorflow-syntaxnet). To install use:

```
docker pull nardeas/tensorflow-syntaxnet
```

### Processing
Some tweets turned out to be empty, after preprocessing we retain a total of 116,882 (this is the
current number of saved items in the parsed tweets file). And then drop again to ~98k after
removing duplicates.

### Better model ([source](https://github.com/tensorflow/models/issues/1347))
"`parsey_mcparseface` was trained on a significantly larger dataset. Further, it was optimized to
maximize both POS tagging accuracy and parsing accuracy."


## TODO

### Resources
* http://davidsbatista.net/blog/2017/03/25/syntaxnet/
* [Gensim Doc2Vec](https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/doc2vec
-lee.ipynb)

### Questions
* How exactly are they doing preprocessing? I'm guessing stopword removal et al. is done after the
SyntaxNet parser since the parser takes entire sentences as input.

