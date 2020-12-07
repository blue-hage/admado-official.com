#!/usr/local/bin/python3

import os
from flask import render_template, request
from app import app
from werkzeug.utils import secure_filename

FILES_DIR = './files'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = FILES_DIR

def allowed_file(filename):
  return '.' in filename and filename.split('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file():
  if request.method == 'POST':
    if 'design' not in request.files:
      return render_template("msg.html", message="デザインは、JPGファイルでお願い致します。", at="/contact", text="フォームに戻る")
    design = request.files['design']
    if design.filename == '':
      return render_template("msg.html", message="ファイル名が設定されていません。", at="/contact", text="フォームに戻る")
    if design and allowed_file(design.filename):
      filename = secure_filename(design.filename)
      design.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return FILES_DIR + '/' + filename
    else:
      return render_template("msg.html", message="デザインは、JPG、PNG、JPEGファイルでお願い致します。", at="/contact", text="フォームに戻る")
      
  