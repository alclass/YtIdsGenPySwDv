#!/usr/bin/env python3
'''
currentFile = __file__  # May be 'my_script', or './my_script' or
                        # '/home/user/test/my_script.py' depending on exactly how
                        # the script was run/loaded.
realPath = os.path.realpath(currentFile)  # /home/user/test/my_script.py
dirPath = os.path.dirname(realPath)  # /home/user/test
dirName = os.path.basename(dirPath) # test
'''
import os
import sqlite3

class Blob:
  """Automatically encode a binary string."""
  def __init__(self, s):
    self.s = s

  def _quote(self):
    print ('=> passing thru _quote()')
    return "'%s'" % sqlite3.encode(self.s)

def convertToBinaryData(filename):
  #Convert digital data to binary format
  realPath = os.path.realpath(__file__)
  dirPath = os.path.dirname(realPath)
  filepath = os.path.join(dirPath, "data/"+filename)
  with open(filepath, 'rb') as file:
    blobData = file.read()
  return blobData

def insertBLOB(empId, name, photoFilename, resumeFilename):
  try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")
    sqlite_insert_blob_query = """ 
      INSERT INTO 'new_employee'
      ('id', 'name', 'photo', 'resume') VALUES (?, ?, ?, ?)
    """
    empPhoto = convertToBinaryData(photoFilename)
    resume = convertToBinaryData(resumeFilename)
    # Convert data into tuple format
    data_tuple = (empId, name, empPhoto, resume)
    cursor.execute(sqlite_insert_blob_query, data_tuple)
    sqliteConnection.commit()
    print("Image and file inserted successfully as a BLOB into a table")
    cursor.close()
  except sqlite3.Error as error:
    print("Failed to insert blob data into sqlite table", error)
  finally:
    if (sqliteConnection):
      sqliteConnection.close()
      print("the sqlite connection is closed")

def test_mass2():
  insertBLOB(1, "Smith", "smith.png", "smith_resume.txt")
  insertBLOB(2, "David", "david.png", "david_resume.txt")

def test_mass():
  db = sqlite3.connect("test.db")
  cursor = db.cursor()
  cursor.execute("CREATE TABLE if not exists t (b BLOB);")
  s = b"\0" * 50 + b"'" * 50
  cursor.execute('INSERT INTO t VALUES("%s");', Blob(s))
  cursor.execute("SELECT b FROM t;")
  b = cursor.fetchone()[0]
  assert b == s  # b is automatically decoded
  db.close()
  #os.remove("test.db")

if __name__ == '__main__':
  # test_mass()
  test_mass2()
  pass
