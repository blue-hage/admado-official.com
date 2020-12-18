#!/usr/local/bin/python3
import mysql.connector
from flask import request

config = {
  'host':'localhost',
  'user':'bluroom_client',
  'password':'20201213',
  'database':'bluroom_client'
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

def new_client():
  company_id = request.form.get("company_id")
  user_id = request.form.get("user_id")
  design = request.files['design']

  conn = mysql.connector.connect(**config)
  mycursor = conn.cursor()
  sql = 'INSERT INTO test (file_id, company_id, user_id, filename, created_at) VALUES (NULL, %s, %s, %s, CURRENT_TIMESTAMP)'
  val = (company_id, user_id, design.filename)
  mycursor.execute(sql, val)
  mycursor.close()
  conn.commit()
  conn.close()
  return design.filename

if __name__ == "__main__":
  exec('INSERT INTO test (file_id, company_id, user_id, filename, created_at) VALUES (NULL, %s, %s, %s, CURRENT_TIMESTAMP)', "adMado", "user", "about.png")