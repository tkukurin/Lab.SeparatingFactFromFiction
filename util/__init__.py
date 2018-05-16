import functools

def compose(*fs):
  return lambda value: \
    functools.reduce(lambda v, f: f(v), fs, value)


def flatten_2d(list_):
  return [item for sublist in list_ for item in sublist]

