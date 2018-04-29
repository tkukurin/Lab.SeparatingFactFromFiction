import sklearn as sk
from collections import namedtuple

Eval = namedtuple('Eval', 'f1_micro f1_macro accuracy')
def scorer(y_true, y_pred):
  f1_micro = sk.metrics.f1_score(y_true, y_pred, average='micro')
  f1_macro = sk.metrics.f1_score(y_true, y_pred, average='macro')
  accuracy = sk.metrics.accuracy_score(y_true, y_pred)

  return Eval(f1_micro, f1_macro, accuracy)

