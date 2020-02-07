#!/usr/bin/python3

# Create jurl table
import sqlite3
def main():

  fn = 'jurl.sql'
  dbn = 'jurl.db'
  sql = get_sql(fn)    
  execute_sql(dbn,sql)

def get_sql(fn):
  f = open(fn,'r')
  sql= str(f.read())
  f.close()
  return sql
  
def execute_sql(dbn, sql):
  db = sqlite3.connect(dbn)
  cur = db.cursor()
  
  print(f'USE {dbn} \n {sql}')
  cur.execute(sql)
  
  db.close()
 

 
 
if __name__=='__main__': main()