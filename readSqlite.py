#!/usr/bin/env python3
'''

'''
import os, sqlite3
#import lib.functions.str_adjust_functions as adjfuns
#from lib.classes.DBModelrClass import DBModel
#from lib.classes.YtIdGeneratorClass import YtIdGenerator
from lib.classes.YtIdGeneratorClass import YtIdDBReader

def process():
  '''

  :return:
  '''
  ytidReader = YtIdDBReader()
  ytids = ytidReader.readAll()
  for i, ytid in enumerate(ytids):
    print (i+1, ytid)

def getArgs():
  n_generate = n_generate_DEFAULT
  bool_store_on_disk = bool_store_on_disk_DEFAULT
  for arg in sys.argv:
    if arg.startswith('-n='):
      try:
        n_generate = int(arg[len('-n='):])
      except ValueError:
        pass
    elif arg.startswith('-s='):
      try:
        yes_or_no = arg[len('-s='):]
        if yes_or_no == 'n':
          bool_store_on_disk = False
      except ValueError:
        pass
  return n_generate, bool_store_on_disk



if __name__ == '__main__':
  process()
