#!/usr/bin/env python3
'''

'''
import os, sqlite3
import lib.functions.str_adjust_functions as adjfuns
from lib.classes.DBModelrClass import DBModel

def test_mass2():
  dbfilepath = os.path.abspath('.')
  model = DBModel(dbfilepath)
  model.printAll()

def test_mass():
  conn = sqlite3.connect('ytids.sqlite')
  cursor = conn.cursor()
  rs = cursor.execute('select ytid from ytids order by ytid')
  for r in rs:
    print (r)


if __name__ == '__main__':
  test_mass()
