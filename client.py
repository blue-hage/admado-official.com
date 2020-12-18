#!/usr/local/bin/python3

import os
from flask import request
# from werkzeug.utils import secure_filename
import sql

FILES_DIR = './files'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(name, design, company_id):
  if name == "No":
    return "no file"

  if design and allowed_file(design.filename):
    picId = sql.select('SELECT * FROM test WHERE filename = %s AND company_id = %s', name, company_id)
    print(picId[0])
    filename = picId[0] + "_" + name
    # filename = name
    design.save(os.path.join(FILES_DIR, filename))
    return FILES_DIR + '/' + filename