#!/usr/local/bin/python3
import os

FILES_DIR = './files'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(name, design, file_id):
  # if name == "No":
  #   return "no file"

  if design and allowed_file(design.filename):
    filename = file_id + "_" + name
    design.save(os.path.join(FILES_DIR, filename))
    return FILES_DIR + '/' + filename