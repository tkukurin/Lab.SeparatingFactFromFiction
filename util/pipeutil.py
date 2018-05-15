"""
Utils for creating transform-only pipelines
"""

import sklearn.pipeline as pipe
from sklearn.pipeline import make_union, make_pipeline
from sklearn.pipeline import FeatureUnion, Pipeline


class Transform(pipe.TransformerMixin):
    def __init__(self, f, name=''):
        self.transform = lambda X, y=None: map(f, X)
        self.fit = lambda *any: self


def is_transformer(t):
  return all(x in set(dir(t)) for x in ['fit', 'transform'])


def to_proper_pipeline_form(*list_of_functions, initializer=Transform):
  transform = lambda t: \
    t if is_transformer(t) \
    else initializer(t, name=t.__name__)
  
  return [transform(f) for f in list_of_functions]


def pipe(*list_of_functions):
  wrapped_functions = to_proper_pipeline_form(*list_of_functions)
  return make_pipeline(*wrapped_functions)


def union(*list_of_functions):
  wrapped_functions = to_proper_pipeline_form(*list_of_functions)
  return make_union(*wrapped_functions)

