from collections import defaultdict

def dict_features(tokens, feature_set):
    ret = defaultdict(int)
    for t in tokens:
        if t in feature_set:
            ret[t] += 1
    return ret


from nltk.tokenize import RegexpTokenizer
from util import data_process, functions
from nltk.stem.porter import PorterStemmer
from sklearn.pipeline import TransformerMixin


class TokenizerTransformer(TransformerMixin):
    
    def __init__(self):
        self.normalizer = data_process.TweetNormalizer()
        self.regex_word_tokenizer = RegexpTokenizer(r'[@]?\w+')
        stemmer = PorterStemmer()
        stem = lambda ws: [stemmer.stem(w) for w in ws]
        self.pipeline = util.compose(
            self.normalizer.transform,
            self.regex_word_tokenizer.tokenize,
            # 10 times faster without stemming 
            # stem,
        )
        
        self.fit = functions.const(self)
        self.transform = self.pipeline

