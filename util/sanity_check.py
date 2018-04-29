import logging
import numpy as np
import pandas as pd
import scipy as sp
import scipy.sparse

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def log_enable():
  log.setLevel(logging.DEBUG)

def log_disable():
  log.setLevel(logging.ERROR)

t_list = lambda o: isinstance(
    o, (list, tuple, np.ndarray, pd.Series, sp.sparse.csr_matrix, ))
t_data = lambda o: isinstance(o, (pd.DataFrame, dict, ))


def noraise(func, except_type=Exception, error_handler=lambda e: None):
  try: func()
  except except_type as e:
    error_handler(e)


xs_numeric_valid = lambda xs: not np.isnan(xs) and not np.isinf(xs)


def check(xs, name='xs', do_log_fst_el=True):
  log.debug('==' + ('=' * len(name)) + '==')
  log.debug('  %s  ', name)
  log.debug('==' + ('=' * len(name)) + '==')

  if t_list(xs):
    xs_1d = np.ravel(xs)
    log.debug('Shape %s', np.shape(xs))
    log.debug('Data type %s', xs_1d.dtype)
    log.debug('1st element: "%s (Type %s)"',
        xs_1d[0] if len(xs_1d) and do_log_fst_el else '??',
        type(xs_1d[0]) if len(xs_1d) else None)

    noraise(lambda: log.debug('NaNs found') if np.isnan(xs_1d) else None,
        error_handler=lambda e: log.debug('raised %s', e))
    noraise(lambda: log.debug('Infs found') if np.isinf(xs_1d) else None,
        error_handler=lambda e: log.debug('raised %s', e))
  if t_data(xs):
    nulls_sum = xs.isnull().sum()
    if nulls_sum.any():
      log.debug('Found nulls: \n%s', nulls_sum)
