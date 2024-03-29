#!/usr/local/bin/python3
from flask import session, redirect, request, render_template, Blueprint
import sql, hashlib, base64, os

admin = Blueprint("admin", __name__, url_prefix="/admin", template_folder="templates", static_folder="static")

REGI_PASS = "20201223_admado4649"
MASTER_PASS = "20201219_admado3150"

def is_login():
  return 'login' in session

def try_login(form):
  user = form.get("user_id", "")
  password = bytes(form.get("password", ""), "utf-8")
  if user == "" or password == "": return False

  correct = sql.select("SELECT * FROM admin WHERE user_id = %s", user)
  if len(correct) == 0: return False

  corr_user = correct[0][1]
  from_data = correct[0][2] + correct[0][3]

  hashed_one = hashlib.pbkdf2_hmac("sha256", password, bytes(correct[0][3], "utf-8"), 1000)
  from_user = hashed_one.hex() + correct[0][3]

  if user != corr_user: return False
  if from_user != from_data: return False

  session['login'] = user
  return True

def new_admin(form):
  user = form.get("user_id", "")
  password = bytes(form.get("password", ""), "utf-8")
  regi_pass = form.get("regi-password", "")

  if user == "" or password == "": return False
  if regi_pass != REGI_PASS: return False
  
  salt = base64.b64encode(os.urandom(32))
  hashed_one = hashlib.pbkdf2_hmac("sha256", password, salt, 1000)
  admin_id = sql.exec("INSERT INTO admin (user_id, password, salt) VALUES (%s, %s, %s)", user, hashed_one.hex(), salt)
  
  session["login"] = user
  return True

# admin page
@admin.route("/list")
def admin_list():
  if request.args.get("admin_pass", "") !=  MASTER_PASS: return redirect("/")
  return render_template("admin_login.html")

@admin.route("/list/try", methods=["POST"])
def admin_login():
  ok = try_login(request.form)
  if not ok: return redirect("/admin/list")
  return redirect("/admin/list/secret")

@admin.route("/list/secret")
def admin_client():
  if not is_login(): redirect("/admin/list")
  clients = sql.select("SELECT * FROM clients")
  return render_template("client_list.html", client_list=clients)


#admin registration
@admin.route("/list/register")
def admin_register():
  if request.args.get("admin_pass", "") != MASTER_PASS: return redirect("/")
  return render_template("admin_register.html")

@admin.route("/list/register/try", methods=["POST"])
def admin_register_try():
  ok = new_admin(request.form)
  if not ok: return redirect("/admin/list/register")
  return redirect("/admin/list/secret")