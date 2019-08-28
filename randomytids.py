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

conn = sqlite3.connect("TestFetches.db")
cur = conn.cursor()
#isPresent = cur.execute( "SELECT target FROM stringList WHERE target='specificString';" ).fetchall()


'''
# import random, sqlite3, string
# import lib.functions.str_adjust_functions as strfuns
from lib.classes.YtIdGeneratorClass import YtIdGenerator

def process():
  '''

  :return:
  '''
  # parameters
  n_of_ytids_to_generate = 100
  # if bool_store_ytids_on_disk is False, all ids will be kept on RAM
  # if bool_store_ytids_on_disk is True, all ids will be kept on disk in Sqlite
  bool_store_ytids_on_disk = False
  
  YtIdGenerator(n_generate = 100, bool_store_on_disk = False)

if __name__ == '__main__':
  process()
