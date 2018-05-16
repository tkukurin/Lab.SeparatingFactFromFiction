import numpy as np


def load_glove(fname):
    glove = {}
    with open(fname) as f:
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            glove[word] = coefs
    return glove


def glove_to_embedding_matrix(glove_200, word_index):
  embedding_dim = 200
  embedding_matrix = np.zeros((num_words, embedding_dim))

  for word, i in word_index.items():
      embedding_vector = glove_200.get(word)
      if embedding_vector is not None:
          embedding_matrix[i] = embedding_vector

  return embedding_matrix

