#!/usr/local/bin/python3
import mysql.connector

config = {
  'host':'localhost',
  'user':'bluroom_client',
  'password':'20201213',
  'database':'bluroom_client'
}

company_id = "adMado_"
user_id = "太郎_"
filename = "admado.png"
conn = mysql.connector.connect(**config)
mycursor = conn.cursor()
sql = 'INSERT INTO test (file_id, company_id, user_id, filename, created_at) VALUES (NULL, %s, %s, %s, CURRENT_TIMESTAMP)'
val = (company_id, user_id, filename)
mycursor.execute(sql, val)
mycursor.close()
conn.commit()
conn.close()