import re, os
from flask import render_template

BASE_DIR = os.path.dirname(__file__)
FILES_DIR = BASE_DIR + '/files'

def save_file(upfile):
  if not re.search(r'\.(jpg|jpeg)$', upfile.filename):
    return render_template("msg.html", message="デザインは、JPGファイルでお願い致します。", at="/contact", text="フォームに戻る")
  upfile.save(os.path.join(FILES_DIR, upfile.filename))
  