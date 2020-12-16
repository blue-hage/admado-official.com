#!/usr/local/bin/python3

import os
from flask import render_template, request
from werkzeug.utils import secure_filename
import sql

FILES_DIR = './files'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file():
  if not request.files:
    return "ok"
  design = request.files['design']

  if design and allowed_file(design.filename):
    filename = secure_filename(design.filename)
    new = sql.new_client(request.args)
    if new == 0: return 0
    filename = sql.select('SELECT file_id FROM clients WHERE filename = ?', filename) + "_" + filename
    design.save(os.path.join(FILES_DIR, filename))
    return FILES_DIR + '/' + filename
      
  