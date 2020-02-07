#!/usr/bin/env python3

import sqlite3

def main():
  # SQL Statements
  sql_drop = 'DROP TABLE IF EXISTS test'
  sql_create = """
    CREATE TABLE test (
      id INTEGER PRIMARY KEY, string TEXT, number INTEGER
    )
    """
  sql_insert1 = """
    INSERT INTO test (string,number) VALUES ('one', 1)
    """
  sql_insert2 = """
    INSERT INTO test (string,number) VALUES ('two', 2)
    """
  sql_insert3 = """
    INSERT INTO test (string,number) VALUES ('three', 3)
    """
  sql_count = 'SELECT COUNT(*) FROM test'
  sql_select = 'SELECT * FROM test'
  
  #SQL Execution  
  print('connect')
  db = sqlite3.connect('db-api.db')
  cur = db.cursor()
  print('create')
  cur.execute(sql_drop)
  cur.execute(sql_create)
  print('insert row')
  cur.execute(sql_insert1)
  print('insert row')
  cur.execute(sql_insert2)
  print('insert row')
  cur.execute(sql_insert3)
  print('commit')
  db.commit()
  print('count')
  cur.execute(sql_count)
  count = cur.fetchone()[0]
  print(f'there are {count} rows in the table.')
  print('read')
  for row in cur.execute(sql_select):
    print(row)
  print('drop')
  cur.execute(sql_drop)
  print('close')
  db.close()
  
if __name__ == '__main__': main()


