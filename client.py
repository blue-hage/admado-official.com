#!/usr/local/bin/python3
import os, mail, sql
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, redirect

client = Blueprint("client", __name__, url_prefix="/client", template_folder="templates", static_folder="static")

FILES_DIR = './files'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(name, design, file_id):
  if name == "無し":
    return [None, "無し"]

  if design and allowed_file(design.filename):
    filename = file_id + "_" + name
    design.save(os.path.join(FILES_DIR, filename))
    return [FILES_DIR + '/' + filename, filename]
  else:
    return [None, "無し"]

@client.route("/try", methods=["POST"])
def client_try():
  email = request.form.get("email")
  tel = request.form.get("tel")
  company_id = request.form.get("company_id")
  user_id = request.form.get("user_id")
  contents = request.form.get("contents")

  if request.files["design"]:
    design = request.files["design"]
    filename = secure_filename(design.filename)
  else:
    design = None
    filename = "無し"

  file_id = str(sql.exec("INSERT INTO clients (company_id, user_id, filename) VALUES (%s, %s, %s)", company_id, user_id, filename))
  attach = save_file(filename, design, file_id)

  msg = mail.client_create(email, tel, company_id, user_id, contents, attach[0], filename, attach[1])
  return redirect("/finished/client")