"""
This module aims to structurize abstracts. For each function, please use the model
in the github repository:
https://github.com/Justin-Jonany/SciDigest/blob/cd3b5cb55b28d70c86556c8254db50afc05bfb47/best_model.keras

Requirements:
1. TensorFlow Library
2. nltk punkt library
"""
# =====================================================================
# Helper function
def split_chars(text):
  """
  Adds a space (' ') in between every character in text
  """
  return " ".join(list(text))
# =====================================================================

def data_preprocess(paragraph, verbose=0):
  """
  Preprocesses the paragraph into the correct format for the model

  Args:
    paragraph: the abstract in form of a string
    verbose: 0 for no information, 1 for information while preprocessing

  Returns:
    A list of data with 4 items in the following order:
      1. A list of line number of each sentence in the abstract one hot encoded
      2. A list with the same object, the total number of lines, as long as the number
        of sentences
      3. A list of every sentence in the abstract
      4. A list of list of characters of each sentences
      5. A list of every sentence without any preprocessing
  """

  import nltk
  # nltk.download('punkt')
  # run the code above first separately
  import tensorflow as tf
  import re

  # From the paragraph we need to get
  # 1. A list of line number of each sentence in the abstract one hot encoded
  # 2. A list with the same object, the total number of lines, as long as the number
  #    of sentences
  # 3. A list of every sentence in the abstract
  # 4. A list of list of characters of each sentences
  # 5. A list of every sentence without any preprocessing


  # 5. A list of every sentence without any preprocessing
  list_sentences_original = nltk.tokenize.sent_tokenize(paragraph)

  # We now need to replace every number in the sentence with '@'
  paragraph = re.sub(r'\d', '@', paragraph)

  # 3. A list of every sentences in the abstract
  # Using the nltk library to effectively separate the sentences
  list_sentences = nltk.tokenize.sent_tokenize(paragraph)

  # 1. A list of line number of each sentence in the abstract one hot encoded
  NUM_CATEGORIES_LN = 15 # set to 15 by default based on the training data
  list_ln = [i for i in range(len(list_sentences))]
  list_ln = tf.one_hot(list_ln, depth=NUM_CATEGORIES_LN)


  # 2. A list with the same object, the total number of lines, as long as the number
  #    of sentences
  NUM_CATEGORIES_TNL = 20 # set to 20 by default based on the training data
  list_total_lines = [len(list_sentences)] * len(list_sentences)
  list_total_lines = tf.one_hot(list_total_lines, depth=NUM_CATEGORIES_TNL)


  # 4. A list of list of characters of each sentences
  list_char_sentences = [split_chars(sentence) for sentence in list_sentences]

  if verbose == 1:
    print('=========================')
    print('\nlist of setences:')
    [print(i) for i in list_sentences]
    print('\nlist of one hot encoded line numbers:')
    print(list_ln)
    print('\nlist of one hot encoded total number of lines:')
    print(list_total_lines)
    print('\nlist of sentences with characters separated:')
    [print(i) for i in list_char_sentences]
    print('=========================')

  return [list_ln, list_total_lines, tf.constant(list_sentences), tf.constant(list_char_sentences),
          list_sentences_original]

def strucurizer(model, data):
  """
  Turns data into a structured abstract

  Args:
    model: A machine learning model
    data: list of data with 4 items in the following order:
      1. A list of line number of each sentence in the abstract one hot encoded
      2. A list with the same object, the total number of lines, as long as the number
        of sentences
      3. A list of every sentence in the abstract
      4. A list of list of characters of each sentences
      5. A list of every sentence without any preprocessing

  Returns:
    Groups of sentences or a sentence is assigned a type of sentence which could be background,
    methods, results, conclusions, or objective. Returned in the format of a dataframe.
  """
  import tensorflow as tf
  import pandas as pd

  class_names = ['BACKGROUND', 'CONCLUSIONS', 'METHODS', 'OBJECTIVE', 'RESULTS', ]

  # predict
  pred_probs = model.predict(x=tuple(data[:-1]), verbose=0)
  preds = [class_names[i] for i in tf.argmax(pred_probs, axis=1)]

  # format data and prediction
  list_sentences = [sentence.numpy().decode(('utf-8')) for sentence in data[2]]
  structured_abstract = pd.DataFrame({'Sentences': list_sentences, 'Target': preds})

  # Printing and Compacting the structured abstract df
  temporary_sentence = ''
  structured_abstract_combined = pd.DataFrame({'Sentences': [], 'Target': []})
  i = 0
  print('')
  print('Structured Abstract')
  print('')
  while (i < len(list_sentences)):
    print(preds[i])
    temporary_sentence = list_sentences[i]
    j = i
    print(data[-1][j])
    while((j < (len(list_sentences) - 1)) and (preds[j] == preds[j+1])):
      print(data[-1][j+1])
      temporary_sentence += data[-1][j+1]
      j += 1
      i += 1
    i+= 1
    print('\n')
    structured_abstract_combined.loc[len(structured_abstract_combined)] = [temporary_sentence, preds[j]]

  return structured_abstract_combined

def preprocess_and_strucurizer(paragraph, model, verbose=0):
  '''
  Preprocesses paragraph (the abstract) and structurize it.

  Args:
    model: A machine learning model
    paragraph: the abstract in form of a string
    verbose: 0 for no information, 1 for information while preprocessing

  Returns:
    Groups of sentences or a sentence is assigned a type of sentence which could be background,
    methods, results, conclusions, or objective. Returned in the format of a dataframe.
  '''
  data = data_preprocess(paragraph, verbose)
  structured_abstract = strucurizer(model, data)
  return structured_abstract
