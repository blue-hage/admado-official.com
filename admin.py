#!/usr/local/bin/python3
from flask import session, redirect
import sql, hashlib, base64, os
from functools import wraps

REGI_PASS = "20201223_admado4649"

def is_login():
  return 'login' in session

def try_login(form):
  user = form.get("user_id")
  password = form.get("password")

  correct = sql.select("SELECT * FROM admin WHERE user_id = %s", user)
  if len(correct) == 0: return False
  corr_user = correct[0][1]
  corr_pass = hashlib.pbkdf2_hmac("sha256", correct[0][2], correct[0][3], 1000)

  if user != corr_user: return False
  if password != corr_pass: return False

  session['login'] = user
  return True

def new_admin(form):
  user = form.get("user_id")
  password = form.get("password")
  regi_pass = form.get("regi-password")

  if regi_pass != REGI_PASS: return False
  
  salt = base64.b64encode(os.urandom(32))
  hashed_one = hashlib.pbkdf2_hmac("sha256", password, salt, 1000)
  admin_id = sql.exec("INSERT INTO admin (user_id, password, salt) VALUES (%s, %s, %s)", user, password, salt)
  
  session["login"] = user
  return True


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_login():
            return redirect('/admin/client/list')
        return func(*args, **kwargs)
    return wrapper