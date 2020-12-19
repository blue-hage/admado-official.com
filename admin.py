#!/usr/local/bin/python3
from flask import session, redirect
import sql
from functools import wraps

def is_login():
  return 'login' in session

def try_login(form):
  user = form.get("user_id")
  password = form.get("password")

  correct = sql.select("SELECT * FROM admin WHERE user_id = %s", user)
  corr_user = correct[0][1]
  corr_pass = correct[0][2]

  if user != corr_user:
    return False
  if password != corr_pass:
    return False

  session['login'] = user
  return True

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_login():
            return redirect('/')
        return func(*args, **kwargs)
    return wrapper

if __name__ == "__main__":
  user = "blue"
  correct = sql.select("SELECT * FROM admin WHERE user_id = %s", user)
  corr_user = correct[0][1]
  corr_pass = correct[0][2]
  print(corr_user, corr_pass)