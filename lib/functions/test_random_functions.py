#!/usr/bin/env python3
'''
  test_str_adjust_functions.py

  Test of Functions for checking or adjusting strings.
'''
import unittest, string
# import lib.functions.str_adjust_functions as adjfuns
import lib.functions.random_functions as ranfuns
class RandomRelatedTest(unittest.TestCase):

  def test_generate_a_64base_11char_id(self):
    '''
    '''
    result = ranfuns.generate_a_64base_11char_id()
    # 1st subtest: restr_id should have 11 characters
    self.assertEqual(len(result), 11)
    for c in result:
      # 2nd subtest: each character should belong to the BASE64CHARACTERS set
      self.assertIn(c, ranfuns.BASE64CHARACTERS)

  def test_generate_a_64base_11char_id_restricted(self):
    '''
    1st restriction is 3rd subtest:
      there should be at least one Uppercase letter in word_id
    2nd restriction is 4th subtest:
      there should be at least one lowercase letter in word_id
    :return:
    '''
    restr_id = ranfuns.generate_a_64base_11char_id_with_the_2_restrictions()
    # 1st subtest: restr_id should have 11 characters
    self.assertEqual(len(restr_id), 11)
    for c in restr_id:
      # 2nd subtest: each character should belong to the BASE64CHARACTERS set
      self.assertIn(c, ranfuns.BASE64CHARACTERS)
    bool_elems = list(map(lambda c : c in string.ascii_uppercase, restr_id))
    # 3rd subtest: there should be at least one Uppercase letter in word_id
    self.assertTrue(True in bool_elems)
    bool_elems = list(map(lambda c : c in string.ascii_lowercase, restr_id))
    # 4th subtest: there should be at least one lowercase letter in word_id
    self.assertTrue(True in bool_elems)

def test_is_it_a_restricted_64base11charid(self):
  word = 'i3b5cQyudgs'
  result = ranfuns.is_it_a_restricted_64base11charid(word)
  self.assertTrue(result)
  word = 'i3b5cqyudgs100000000'
  result = ranfuns.is_it_a_restricted_64base11charid(word)
  self.assertFalse(result)

  word = 'i3b5cqyudgs100000000'
  result = ranfuns.is_it_a_restricted_64base11charid(word)
  self.assertFalse(result)

  word = 'i3b5c*yudgs' # the * is not a base64 valid character
  self.assertEqual(len(word), 11)
  result = ranfuns.is_it_a_restricted_64base11charid(word)
  self.assertFalse(result)

  word = 'I3B5CQYUDGS'
  self.assertEqual(len(word), 11)
  result = ranfuns.is_it_a_restricted_64base11charid(word)
  self.assertFalse(result)

  word = 'i3b5cqyudgs'
  self.assertEqual(len(word), 11)
  result = ranfuns.is_it_a_restricted_64base11charid(word)
  self.assertFalse(result)
