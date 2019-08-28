#!/usr/bin/env python3
'''

'''
import os
import lib.functions.str_adjust_functions as adjfuns
from lib.classes.DBModelrClass import DBModel

def test_mass():
  d = '''9heq1CEGjCP
         fGGPu3D5RW1
         94egIi22Ppw
         e6v236T1aMO
         5x5snfxLI5G'''
  entries = adjfuns.clean_entries_borders_with_linesplit(d)
  dbfilepath = os.path.abspath('.')
  # print ('dbfilepath', dbfilepath)
  model = DBModel(dbfilepath)
  for e in entries:
    model.insert_a_ytid(e)
  model.close()

if __name__ == '__main__':
  test_mass()
