#!/usr/bin/env python3
'''
  str_adjust_functions.py

  Functions for checking or adjusting strings.
'''
# lambda-based functions
lamb_clean_borders = lamb_clean_borders = lambda c : c.strip(' \t\r\n')
def clean_entry_borders(entries):
  if entries is None or entries == []:
    return []
  if type(entries) not in [list, tuple]:
    error_msg = str(entries)
    raise ValueError(error_msg)
  return list(map(lamb_clean_borders, entries))
  
def clean_entries_borders_with_linesplit(text):
  if text is None or text == '':
    return []
  if len(text) == 0: # notice that it can be other than a string here (a list, a dict etc)
    return []
  text = str(text)
  text = text.strip(' \t\r\n')
  entries = text.split('\n')
  if entries == []:
    return []
  return clean_entry_borders(entries)

def isItAllNumbers(word):
  '''
    Check whether a word is composed of integer numbers.
    Inside the native int() does the job.
    If a ValueError exception is raised, False is returned.
  '''
  if type(word) not in [int, float, str]:
    # a (simple) boolean is not allowed, a string is allowed if it's composed of numbers
    return False
  try:
    int(word)
    return True
  except ValueError:
    pass
  return False

def modify_word_with_char_at_position(word, character, indexAt):
  '''

  :param word:
  :param character:
  :param indexAt:
  :return:
  '''
  if indexAt > len(word) - 1:
    indexAt = indexAt % len(word)
  if indexAt <= 0:
    indexAt = 0
    word = character + word[1:]
  elif indexAt == len(word) - 1:
    word = word[ : indexAt] + character
  else:
    word = word[ : indexAt] + character + word[indexAt + 1 : ]
  print ('AFTER: ', word)
  return word

def swap_one_random_lowercaseletter_to_an_Uppercaseletter(word):
  '''
  '''
  print ('BEFORE: ', word, ' <= to Upper')
  charlist = list(word)
  islowercasefound = False
  while len(charlist) > 0:
    indexAt = random.randint(0, len(charlist)-1)
    supposedlowercaseletter = charlist[indexAt]
    if not supposedlowercaseletter in string.ascii_lowercase:
      del charlist[indexAt]
      continue
    else:
      islowercasefound = True
      lowercaseletter = supposedlowercaseletter
      break
  if not islowercasefound:
    #return False
    error_msg = 'Failed in swap_one_random_lowercaseletter_to_an_Uppercaseletter() lowercase not found in %s' %self.ytid
    raise ValueError(error_msg)
  indexAt = self.ytid.index(lowercaseletter)
  Uppercaseletter = lowercaseletter.upper()
  word = strfuns.modify_word_with_char_at_position(word, Uppercaseletter, indexAt)
  return word


def swap_one_random_Uppercaseletter_to_a_lowercaseletter(word):
  '''
  '''
  print ('BEFORE: ', word, ' <= to lower')
  charlist = list(word)
  isUppercasefound = False
  while len(charlist) > 0:
    indexAt = random.randint(0, len(charlist)-1)
    supposedUppercaseletter = charlist[indexAt]
    if not supposedUppercaseletter in string.ascii_uppercase:
      del charlist[indexAt]
      continue
    else:
      isUppercasefound = True
      Uppercaseletter = supposedUppercaseletter
      break
  if not isUppercasefound:
    #return False
    error_msg = 'Failed in swap_one_random_Uppercaseletter_to_a_lowercaseletter() Uppercase not found in %s' %self.ytid
    raise ValueError(error_msg)
  # the indexAt above may be wrong, because the while-loop may delete elements; the downside is if a letter is repeated, what is, on the same token, very unlikely
  indexAt = self.ytid.index(Uppercaseletter)
  lowercaseletter = Uppercaseletter.lower()
  word = strfuns.modify_word_with_char_at_position(word, lowercaseletter, indexAt)
  return word
