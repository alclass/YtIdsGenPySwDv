#!/usr/bin/env python3
'''
  test_str_adjust_functions.py

  Test of Functions for checking or adjusting strings.
'''
import unittest
import lib.functions.str_adjust_functions as adjfuns

class AdjustTest(unittest.TestCase):

  def test_isItAllNumbers(self):
    '''
      Check whether a word is composed of integer numbers.
      Inside the native int() does the job.
      If a ValueError exception is raised, False is returned.
    '''
    self.assertTrue (adjfuns.isItAllNumbers(10))
    self.assertTrue (adjfuns.isItAllNumbers('10'))
    self.assertFalse(adjfuns.isItAllNumbers('a'))
    self.assertFalse(adjfuns.isItAllNumbers(True))
    self.assertFalse(adjfuns.isItAllNumbers(False))
    self.assertFalse(adjfuns.isItAllNumbers({1:'a'}))

  def test_modify_word_with_char_at_position(self):
    '''

    :param word:
    :param character:
    :param indexAt:
    :return:
    
    '''
    word     = 'test'
    newchar  = 'E'
    indexAt  = 1
    expected = 'tEst'
    result   = adjfuns.modify_word_with_char_at_position(word, newchar, indexAt)
    self.assertEqual(expected, result)
    word     = 'blah blah 123 áü'
    newchar  = 'â'
    indexAt  = 7
    expected = 'blah blâh 123 áü'
    result   = adjfuns.modify_word_with_char_at_position(word, newchar, indexAt)
    word     = 'blah blah 123 áü'
    newchar  = 'â'
    indexAt  = 7000
    # expectedIndexAt = 7000 % len('blah blah 123 áü')
    # expectedIndexAt is = to 8
    expected = 'blah blaâ 123 áü'
    result   = adjfuns.modify_word_with_char_at_position(word, newchar, indexAt)
    word     = 'blah blah 123 áü'
    newchar  = 'Ä'
    indexAt  = 15
    expected = 'blah blâh 123 áÄ'
    result   = adjfuns.modify_word_with_char_at_position(word, newchar, indexAt)
    word     = 'Dig New World'
    newchar  = 'B'
    indexAt  = -15 # a negative number should become 0 inside function
    expected = 'Big New World'
    result   = adjfuns.modify_word_with_char_at_position(word, newchar, indexAt)

  def test_clean_entry_borders(self):
    '''
    '''
    entries = [
        '  \t 9heq1CEGjCP',
        'fGGPu3D5RW1 \t\n',
        '  5x5snfxLI5G  '
      ]
    result = adjfuns.clean_entry_borders(entries)
    expected = [
        '9heq1CEGjCP',
        'fGGPu3D5RW1',
        '5x5snfxLI5G'
      ]
    self.assertEqual(expected, result)
    
    result = adjfuns.clean_entry_borders(None)
    self.assertEqual([], result)
    
    result = adjfuns.clean_entry_borders([])
    self.assertEqual([], result)


  def test_clean_entries_borders_with_linesplit(self):
    '''
    '''
    d = '''9heq1CEGjCP
         fGGPu3D5RW1
         5x5snfxLI5G'''
    entries = adjfuns.clean_entries_borders_with_linesplit(d)
    expected = [
        '9heq1CEGjCP',
        'fGGPu3D5RW1',
        '5x5snfxLI5G'
      ]
    self.assertEqual(entries, expected)

    result = adjfuns.clean_entries_borders_with_linesplit(None)
    self.assertEqual([], result)
    
    result = adjfuns.clean_entries_borders_with_linesplit('')
    self.assertEqual([], result)

    result = adjfuns.clean_entries_borders_with_linesplit([])
    self.assertEqual([], result)
