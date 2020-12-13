#!/usr/local/bin/python3

import mysql.connector
config = {
  'host':'localhost',
  'user':'bluroom_client',
  'password':'20201213',
  'database':'bluroom_client'
}
conn = mysql.connector.connect(**config)
print(conn.is_connected())