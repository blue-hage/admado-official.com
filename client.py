#!/usr/local/bin/python3

import os
from flask import request
# from werkzeug.utils import secure_filename
import sql

FILES_DIR = './files'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file():
  if not request.files:
    return "no file"

  design = request.files['design']
  company_id = request.form.get("company_id", "")
  user_id = request.form.get("user_id", "")
  origin = request.form.get("design", "")

  if design and allowed_file(origin):
    head = sql.new_client(company_id, user_id, origin)
    filename = head + "_" + origin
    design.save(os.path.join(FILES_DIR, filename))
    return FILES_DIR + '/' + filename
      
  