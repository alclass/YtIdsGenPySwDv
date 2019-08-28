#!/usr/bin/env python3
'''

'''
import os
import sqlite3
import lib.functions.str_adjust_functions as adjfuns

# import lib.functions.str_adjust_functions as strfuns
# YTIDCHARLENGTH = 11
# base64chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '-' + '_'

DATABASE_FILENAME = 'ytids.sqlite'
TABLENAME = 'ytids'

def get_connection(databasefolderpath=None):
  if databasefolderpath is None or not os.path.isfile(databasefolderpath):
    localpath = os.path.abspath('.')
    dbfilepath = os.path.join(localpath, DATABASE_FILENAME)
  else:
    dbfilepath = os.path.join(databasefolderpath, DATABASE_FILENAME)
  print ('dbfilepath', dbfilepath)
  conn = sqlite3.connect(dbfilepath)
  return conn

def create_table_if_not_exists(conn):
  tablenamedict = {'tablename': DATABASE_FILENAME}
  create_table_str = '''
CREATE TABLE IF NOT EXISTS %(tablename)s  (
	"ytid"	TEXT,
	PRIMARY KEY("ytid")
);
  ''' %tablenamedict
  cursor = conn.cursor()
  cursor.execute(create_table_str)  #cursor.close()
  conn.commit()

class DBModel:

  def __init__(self, databasefolderpath=None):
    self.databasefolderpath = databasefolderpath
    self.set_connection()
    create_table_if_not_exists(self.conn)

  def set_connection(self):
    self.conn = get_connection(self.databasefolderpath)

  def insert_a_ytid(self, ytid):
    insert_interpolated = '''
      INSERT INTO %(tablename)s (ytid) VALUES (:ytid)
    ''' %{'tablename' : TABLENAME}
    
    cursor = self.conn.cursor()
    cursor.execute(insert_interpolated, {'ytid':ytid})
    conn.commit()

  def returnThoseNotInDB(self, entries):
    sql = 'select ytid from ytids where ytid in ('
    for e in entries:
      sql += '"'+e+'",'
    sql = sql.strip(',')
    sql = sql + ')'
    conn = self.get_connection()
    cursor= conn.cursor()
    rs = cursor.execute(sql)
    entriesMissing = list(entries)
    for r in rs:
      entriesMissing.remove(r)
    return entriesMissing

    
    
    


  def printAll(self):
    select_interpolated = '''
      SELECT * FROM %(tablename)s
    ''' %{'tablename' : TABLENAME}
    
    cursor = self.conn.cursor()
    result = cursor.execute(select_interpolated)
    for r in result:
      print (r)

  def close(self):
    self.conn.close()


  
