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
  company_id = "あいあい".decode("utf8")
  user_id = "おいおい".decode("utf8")
  filename = "about.png"
  exec('INSERT INTO test (company_id, user_id, filename) VALUES (%s, %s, %s)', company_id, user_id, filename)
  clients = select("SELECT * FROM test")
  for row in clients:
    print("file_id =", row[0])
    print("company_id =", row[1])
    print("user_id =", row[2])
    print("filename =", row[3])
    print("created_at =", row[4])