def const(out):
  return lambda *x: out


def id():
  return lambda *x: x
