import functools

def compose(*fs):
  return lambda value: \
    functools.reduce(lambda v, f: f(v), fs, value)
