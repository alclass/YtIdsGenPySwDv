#!/usr/bin/env python3
'''

'''
import random, string # sqlite3
import lib.functions.str_adjust_functions as strfuns

YTIDCHARLENGTH = 11
base64chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '-' + '_'
assert 64, len(base64chars)

class YtIdGenerator:
  '''
  '''

  def __init__(self, n_generate=100, bool_store_on_disk = False):
    self.ytid = None
    self.n_generate = n_generate
    self.generate_ytids()

  def generate_ytids(self):
    '''

    :param self:
    :return:
    '''
    for i in range(1, self.n_generate+1):
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

      Not testing for:

      1) all characters are - or _ -> reason: it's very unprobable
      2) all characters are -, _ or numbers -> reason: this id is okay
      3) all characters are lowercsse or Uppercase letters -> reason: this id is okay

      On the same token, ids having
      1) all numbers (first if above),
      2) lowercase letters without at least one Uppercase letter or,
      3) invertedly, Uppercase letters without at least one lowercase letter

      are transformed into the following:

      for 1 above => include 1 Uppercase and 1 lowercase letters
      for 2 above => swap one random lowercase letter to its Uppercase counterpart
      for 3 above => swap one random Uppercase letter to its lowercase counterpart

      There are unittests for these 3 hypotheses.

    :return:
    '''
    #print (ytid)
    if strfuns.isItAllNumbers(self.ytid):
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
    self.ytid = strfuns.modify_word_with_char_at_position(self.ytid, Uppercaseletter, indexAtUpper)
    self.ytid = strfuns.modify_word_with_char_at_position(self.ytid, lowercaseletter, indexAtLower)

  def swap_one_random_lowercaseletter_to_an_Uppercaseletter(self):
    '''

    :return:
    '''
    self.ytid = strfuns.swap_one_random_lowercaseletter_to_an_Uppercaseletter(
        self.ytid
      )

    if self.ytid is not None:
      return True
    return False

  def swap_one_random_Uppercaseletter_to_a_lowercaseletter(self):
    '''

    :return:
    '''
    self.ytid = strfuns.swap_one_random_Uppercaseletter_to_a_lowercaseletter(
        self.ytid
      )

    if self.ytid is not None:
      return True
    return False
