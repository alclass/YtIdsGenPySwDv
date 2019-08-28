#!/usr/bin/env python3
'''
  random_functions.py

  Functions for doing random-related calculations.
'''
import random, string
import lib.functions.str_adjust_functions as strfuns
BASE64CHARACTERS = string.ascii_uppercase + string.ascii_lowercase + string.digits + '-' + '_'
assert 64, len(BASE64CHARACTERS)

def generate_a_64base_11char_id():
  word = ''
  for i in range(0, 11):
    word += random.choice(BASE64CHARACTERS)
  return word

def generate_a_64base_11char_id_with_the_2_restrictions():
  '''
  1st restriction: there should be at least one Uppercase letter in word_id
  2nd restriction: there should be at least one lowercase letter in word_id
  :return:
  '''
  word = generate_a_64base_11char_id()
  word = check_the_2_restrictions_n_modify_id_if_needed(word)
  if word is None or type(word) != str or word == '':
    return None
  return word

def put_a_random_lowercaseletter_in_word(word):
  if word is None or type(word) != str or word == '':
    return None
  size = len(word)
  if size > 1:
    indexAt = random.randint(0, size-1)
  else:
    indexAt = 0
  # lowercaseletter
  character = random.choice(string.ascii_lowercase)
  return strfuns.modify_word_with_char_at_position(word, character, indexAt)

def put_a_random_Uppercaseletter_in_word(word):
  if word is None or type(word) != str or word == '':
    return None
  size = len(word)
  if size > 1:
    indexAt = random.randint(0, size-1)
  else:
    indexAt = 0
  # Uppercaseletter
  character = random.choice(string.ascii_uppercase)
  return strfuns.modify_word_with_char_at_position(word, character, indexAt)

def exists_a_lowercaseletter(word):
  bool_elems = list(map(lambda c: c in string.ascii_lowercase, word))
  if True in bool_elems:
    return True
  return False

def exists_an_Uppercaseletter(word):
  bool_elems = list(map(lambda c: c in string.ascii_uppercase, word))
  if True in bool_elems:
    return True
  return False

def check_the_2_restrictions_n_modify_id_if_needed(word, n_of_tries=1):
  if n_of_tries > 3:
    error_msg = 'Computation error: in function check_the_2_restrictions_n_modify_id_if_needed() => n_of_tries got above 3.'
    raise Exception(error_msg)
  if word is None or type(word) != str or word == '':
    return None
  pass_lower = False
  if exists_a_lowercaseletter(word):
    pass_lower = True
  else:
    word = put_a_random_lowercaseletter_in_word(word)
  pass_upper = False
  if exists_an_Uppercaseletter(word):
    pass_upper = True
  else:
    word = put_a_random_Uppercaseletter_in_word(word)
  if pass_lower and pass_upper:
    return word
  return check_the_2_restrictions_n_modify_id_if_needed(word, n_of_tries+1)

def do_all_chars_belong_to_base64(word):
  for c in word:
    if c not in BASE64CHARACTERS:
      return False
  return True

def is_it_a_restricted_64base11charid(word):
  '''
  There are 4 tests to verify it's a restricted 64base 11char id
  :param word:
  :return:
  '''
  # test 1: size 11
  pass_size = False
  if len(word) == 11:
    pass_size = True
  # test 2: all characters belong to the BASE64 set
  pass_base64 = False
  if do_all_chars_belong_to_base64(word):
    pass_base64 = True
  # test 3: at least one lowercase letter
  pass_lower = False
  if exists_a_lowercaseletter(word):
    pass_lower = True
  # test 4: at least one Uppercase letter
  pass_upper = False
  if exists_a_lowercaseletter(word):
    pass_upper = True
  if pass_size and pass_base64 and pass_lower and pass_upper:
    return True
  return False
