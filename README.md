
## Scraper
Multiclass and binary have overlapping Tweets (multiclass is a subset of binary). Not all Tweets
are available because some accounts were suspended in the meantime. In total, our scraper collected
119,136 of them.


## SyntaxNet
They mention SyntaxNet preprocessing, however I'm not sure where the output gets sent to.

SyntaxNet is installed [via Docker](
https://github.com/tensorflow/models/blob/master/research/syntaxnet/g3doc/CLOUD.md), find sh
convenience scripts in the `syntaxnet` directory.

The file `wrapper.py` is to be run from within a docker container obtained from
[nardeas/tensorflow-syntaxnet](https://github.com/nardeas/tensorflow-syntaxnet). Usage:

```
# install
docker pull nardeas/tensorflow-syntaxnet

# run it.
$ ./syntaxnet/run.sh
$ ./syntaxnet/exec.sh
```

### Processing
Some tweets turned out to be empty, after preprocessing we retain a total of 116,882 (this is the
current number of saved items in the parsed tweets file). And then drop again to ~98k after
removing duplicates.

### Better model ([source](https://github.com/tensorflow/models/issues/1347))
"`parsey_mcparseface` was trained on a significantly larger dataset. Further, it was optimized to
maximize both POS tagging accuracy and parsing accuracy."


## Lexicons and resources
* [Alternative to LIWC](https://www.quora.com/What-is-an-alternative-to-LIWC-software)
* [Positive/Negative words](https://www.quora.com/Is-there-a-downloadable-database-of-positive-and-negative-words)
* [Subjectivity](http://mpqa.cs.pitt.edu/#subj_lexicon)
* [GloVe embeddings](https://nlp.stanford.edu/projects/glove/) (downloaded Twitter)

## TODO

### Resources
* http://davidsbatista.net/blog/2017/03/25/syntaxnet/
* [Gensim Doc2Vec](
https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/doc2vec-lee.ipynb)
  * They train for 15 epochs, 200-dimensional models
* [Example embedding in Keras](https://github.com/bhaveshoswal/CNN-text-classification-keras/blob/master/model.py)
* [ROC/AUC in Keras](https://stackoverflow.com/questions/41032551/how-to-compute-receiving-operating-characteristic-roc-and-auc-in-keras)

