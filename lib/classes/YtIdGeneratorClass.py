#!/usr/bin/env python3
'''

'''
import os, random, string, sqlite3
import lib.functions.str_adjust_functions as strfuns
import lib.functions.random_functions as randf

YTIDCHARLENGTH = 11
base64chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '-' + '_'
assert 64, len(base64chars)

def sqlite_open():
  currentFile = __file__  # May be 'my_script', or './my_script' or
  # '/home/user/test/my_script.py' depending on exactly how
  # the script was run/loaded.
  realPath = os.path.realpath(currentFile)  # /home/user/test/my_script.py
  dirPath = os.path.dirname(realPath)  # /home/user/test
  # dirName = os.path.basename(dirPath)
  sqlite_filename = 'ytids.sql'
  filepath = os.path.join(dirPath, sqlite_filename)
  conn = sqlite3.connect(filepath)
  create_sql = '''
    CREATE TABLE `ytids` (
	    `ytid`	TEXT,
	    PRIMARY KEY(`ytid`)
  );
    '''
  conn.execute(create_sql)
  return conn

class YtIdGenerator:
  '''
  '''

  def __init__(self, n_generate=100, bool_store_on_disk = False):
    self.ytid = None
    self.n_generate = n_generate
    self.conn = False
    self.bool_store_on_disk = bool_store_on_disk
    if self.bool_store_on_disk:
      self.conn = sqlite_open()
    self.generate_ytids()


  def generate_ytids(self):
    '''

    :param self:
    :return:
    '''
    for i in range(1, self.n_generate+1):
      self.generate_ytid()
      self.fix_ytid_if_needed()
      if self.bool_store_on_disk:
        if self.conn:
          sqlinsert = '''
          INSERT INTO ytids (ytid) VALUES (?);
          '''
          cursor = self.conn
          cursor.execute(sqlinsert, self.ytid)
          self.conn.commit()
      print (i, self.ytid)

  def generate_ytid(self):
    self.ytid = ''
    for i in range(0, 11):
      self.ytid += random.choice(base64chars)

  def fix_ytid_if_needed(self):
    '''

      There are only 2 (two) restrictions imposed on ytid, they are:

      1) it must contain at least one lowercase letter
      2) it must contain at least one uppercase letter

      This method modifies a ytid to constrain it to the above two restrictions.

      1) first, an if asks if at least one lowercase letter exists in word, if not, put it there
      2) second, an if asks if at least one uppercase letter exists in word, if not, put it there

      There are unittests for the two restrictions above.

    :return:
    '''
    #print (ytid)
    self.ytid = randf.check_the_2_restrictions_n_modify_id_if_needed(self.ytid)

  def include_one_Upper_n_one_lower(self):
    '''
    This method is no longer used due to having a new strategy (the check 2 restriction function)

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
    This method is no longer used due to having a new strategy (the check 2 restriction function)

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
    This method is no longer used due to having a new strategy (the check 2 restriction function)
    :return:
    '''
    self.ytid = strfuns.swap_one_random_Uppercaseletter_to_a_lowercaseletter(
        self.ytid
      )

    if self.ytid is not None:
      return True
    return False
