#!/usr/local/bin/python3
from sql import exec

exec("""
CREATE TABLE clients(
  file_id INTEGER PRIMARY KEY AUTOINCREMENT,
  company_id TEXT,
  user_id TEXT,
  filename TEXT,
  created_at TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
)
""")

exec("""
CREATE TABLE admin(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id TEXT,
  pwd TEXT
)
""")