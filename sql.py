#!/usr/local/bin/python3
import mysql.connector

config = {
  'host':'localhost',
  'user':'bluroom_client',
  'password':'20201213',
  'database':'bluroom_client',
  'charset':'utf8'
}

def open_db():
  conn = mysql.connector.connect(**config)
  conn.row_factory = dict_factory
  return conn

def dict_factory(cursor, row):
  d = {}
  for idx, col in enumerate(cursor.description):
    d[col[0]] = row[idx]
  return d

def exec(sql, *args):
  db = open_db()
  c = db.cursor()
  c.execute(sql, args)
  db.commit()
  return c.lastrowid

def select(sql, *args):
  db = open_db()
  c = db.cursor()
  c.execute(sql, args)
  return c.fetchall()

if __name__ == "__main__":
  a = select("SELECT * FROM test WHERE company_id = %s", "あいあい")
  print(a[0][0])
  print(a[0][1].encode('utf-8'))
  print(a[0][2].encode('utf-8'))
  print(a[0][3])
  print(a[0][4])