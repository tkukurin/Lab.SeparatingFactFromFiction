from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Input, GlobalMaxPooling1D
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.models import Model
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

def model(embedding_matrix, tokenizer):
  """
  embedding_matrix: matrix of 200-dim GloVe embeddings
  tokenizer: instance of fitted keras.preprocessing.text.Tokenizer
  """
  EMBEDDING_DIM = 200
  MAX_NUM_WORDS = 93038
  MAX_SEQUENCE_LENGTH = 140

  word_index = tokenizer.word_index
  num_words = min(MAX_NUM_WORDS, len(word_index) + 1)

  sequence_input = Input(
      shape=(MAX_SEQUENCE_LENGTH,), dtype='int32')

  embedding_layer = Embedding(
      num_words, EMBEDDING_DIM, weights=[embedding_matrix],
      input_length=MAX_SEQUENCE_LENGTH, trainable=False)

  embedded_sequences = embedding_layer(sequence_input)

  x = Conv1D(128, 5, activation='relu')(embedded_sequences)
  x = MaxPooling1D(5)(x)
  x = Conv1D(128, 5, activation='relu')(x)
  x = GlobalMaxPooling1D()(x)
  x = Dense(128, activation='relu')(x)
  preds = Dense(len(df.label.unique()), activation='softmax')(x)

  model = Model(sequence_input, preds)
  return model
