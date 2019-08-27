#!/usr/bin/env python3
'''

From the page below:
  http://www.learningaboutelectronics.com/Articles/How-to-generate-a-random-video-id-like-youtube-in-Python.php

We learnt two things:
  1) a ytid is a 64-base 11-character string
  2) this 64-base is composed of 26 Uppercase letters, 26 lowercase ones, 10 digits (number) and the caracters '-' and '_'
     it's 26+26=52 plus 10, giving 62, plus - and _, thus, 64 characters

But, there is another detail we have noticed empirically.  A ytid always has
  at least one Uppercase letter or a lowercase letter.

  (It doesn't need to have a number (0-9 digits) or the - or _.

A question: how can it be treated to have at least
 one Uppercase letter or one lowercase one?

 A post treatment might do that.
 After getting it, an if could ask for one Uppercase letter,
 then, it it's missing, randomly including it and another if will do the same
 for the lowercase letter.

'''
import random, sqlite3, string

conn = sqlite3.connect("TestFetches.db")
cur = conn.cursor()
#isPresent = cur.execute( "SELECT target FROM stringList WHERE target='specificString';" ).fetchall()

YTIDCHARLENGTH = 11
base64chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '-' + '_'
assert 64, len(base64chars)

def isItAllNumbers(word):
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
  if indexAt == 0:
    word = character + word[1:]
  elif indexAt == len(word) - 1:
    word = word[ : indexAt] + character
  else:
    word = word[ : indexAt] + character + word[indexAt + 1 : ]
  print ('AFTER: ', word)
  return word

class YtIdGenerator:

  def __init__(self, n_to_generate=10000):
    self.ytid = None
    self.n_to_generate = n_to_generate
    self.generate_ytids()

  def generate_ytids(self):
    '''

    :param self:
    :return:
    '''
    for i in range(1, self.n_to_generate+1):
      self.generate_ytid()
      self.fix_ytid_if_needed()
      assert 11, len(self.ytid)
      print (i, self.ytid)

  def generate_ytid(self):
    self.ytid = ''
    for i in range(0, 11):
      self.ytid += random.choice(base64chars)

  def fix_ytid_if_needed(self):
    '''

      If it's all numbers, include one Uppercase and one lowercase and return
      If word == lower(word), then an Uppercase is missing, get one there and return
      If word == upper(word), then a lowercase is missing, get one there and return

    :return:
    '''
    #print (ytid)
    if isItAllNumbers(self.ytid):
      self.ytid = self.include_one_Upper_n_one_lower()
      return
    if self.ytid == self.ytid.lower():
      self.swap_one_random_lowercaseletter_to_an_Uppercaseletter()
      return
    if self.ytid == self.ytid.upper():
      self.swap_one_random_Uppercaseletter_to_a_lowercaseletter()
      return

  def include_one_Upper_n_one_lower(self):
    '''

    :return:
    '''
    print ('BEFORE: ', self.ytid, ' <= to one Upper n one lower')
    indices_initial_set = list(range(0, YTIDCHARLENGTH - 1))
    indexAtUpper = random.choice(indices_initial_set)
    del indices_initial_set[indexAtUpper]
    indexAtLower = random.choice(indices_initial_set)
    Uppercaseletter = random.choice(string.ascii_uppercase)
    lowercaseletter = random.choice(string.ascii_lowercase)
    self.ytid = modify_word_with_char_at_position(self.ytid, Uppercaseletter, indexAtUpper)
    self.ytid = modify_word_with_char_at_position(self.ytid, lowercaseletter, indexAtLower)

  def swap_one_random_lowercaseletter_to_an_Uppercaseletter(self):
    '''

    :return:
    '''
    print ('BEFORE: ', self.ytid, ' <= to Upper')
    charlist = list(self.ytid)
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
    self.ytid = modify_word_with_char_at_position(self.ytid, Uppercaseletter, indexAt)
    return True

  def swap_one_random_Uppercaseletter_to_a_lowercaseletter(self):
    '''

    :return:
    '''
    print ('BEFORE: ', self.ytid, ' <= to lower')
    charlist = list(self.ytid)
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
    self.ytid = modify_word_with_char_at_position(self.ytid, lowercaseletter, indexAt)

def process():
  '''

  :return:
  '''
  YtIdGenerator()

if __name__ == '__main__':
  process()
