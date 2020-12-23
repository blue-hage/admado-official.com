#!/usr/local/bin/python3
from flask import Flask, render_template, request, redirect
import smtplib, mail, client, admin, sql
from mail import USER_NAME_CLIENT, USER_NAME_CONTACT, PASSWORD_CLIENT, PASSWORD_CONTACT
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "fkldsjt42u815dsfv"

HOST = "om1002.coreserver.jp"
PORT = 465
MASTER_PASS = "20201219_admado3150"

# home page
@app.route("/")
def index_page():
  return render_template("index.html")


# concept page
@app.route("/concept")
def concept_page():
  return render_template("concept.html")


# services page branches
@app.route("/services")
def service_page():
  return render_template("services.html", aria_ge="true", show_ge="show", aria_dri="true", show_dri="show", aria_cli="true", show_cli="show")

@app.route("/services/general")
def general_page():
  return render_template("services.html", aria_ge="true", show_ge="show", aria_dri="false", aria_cli="false")

@app.route("/services/driver")
def driver_page():
  return render_template("services.html", aria_ge="false", aria_dri="true", show_dri="show", aria_cli="false")

@app.route("/services/client")
def client_page():
  return render_template("services.html", aria_ge="false", aria_dri="false", aria_cli="true", show_cli="show")


# aboutus page
@app.route("/aboutus")
def aboutus_page():
  return render_template("aboutus.html")


# contact page
@app.route("/contact")
def contact_page():
  return render_template("contact.html")

@app.route("/contact/try", methods=["POST"])
def contact_try():
  email = request.form.get("email")
  name = request.form.get("name")
  contents = request.form.get("contents")

  msg = mail.contact_create(email, name, contents)
  host = HOST
  port = PORT

  smtp = smtplib.SMTP_SSL(host, port)
  smtp.login(USER_NAME_CONTACT, PASSWORD_CONTACT)
  smtp.send_message(msg[0])
  smtp.send_message(msg[1])
  smtp.quit()
  return redirect("/contact/finished")


# client application page
@app.route("/client")
def client_app_page():
  return render_template("client.html")

@app.route("/client/try", methods=["POST"])
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

  attach = client.save_file(filename, design, file_id)

  msg = mail.client_create(email, tel, company_id, user_id, contents, attach[0], filename, attach[1])
  host = HOST
  port = PORT

  smtp = smtplib.SMTP_SSL(host, port)
  smtp.login(USER_NAME_CLIENT, PASSWORD_CLIENT)
  smtp.send_message(msg[0])
  smtp.send_message(msg[1])
  smtp.quit()
  return redirect("/client/finished")


# policies
@app.route("/policy_user")
def policy_user():
  return render_template("policy_user.html")

@app.route("/policy_pri")
def policy_pri():
  return render_template("policy_pri.html")

@app.route("/policy_ad")
def policy_ad():
  return render_template("policy_ad.html")


# message pages
@app.route("/contact/finished")
def contact_done():
  return render_template("msg.html", message="お問い合わせ完了。確認メールをご確認ください。", at="/", text="ホームに戻る")

@app.route("/client/finished")
def client_done():
  return render_template("msg.html", message="広告掲載の申し込み受付完了。当社からのご連絡をお待ちください。", at="/", text="ホームに戻る")


# admin page
@app.route("/admin/client/list")
def admin_list():
  if request.args.get("admin_pass", "") !=  MASTER_PASS:
    return redirect("/")
  return render_template("admin_login.html")

@app.route("/admin/client/list/try", methods=["POST"])
def admin_login():
  ok = admin.try_login(request.form)
  if not ok: return redirect("/admin/client/list")
  return redirect("/admin/client/list/secret")

@app.route("/admin/client/list/secret")
@admin.login_required
def admin_client():
  clients = sql.select("SELECT * FROM clients")
  return render_template("client_list.html", client_list=clients)


#admin registration
# @app.route("/admin/client/list/register")
# def admin_register():
#   if request.args.get("admin_pass", "") != MASTER_PASS: return redirect("/")
#   return render_template("admin_register.html")

# @app.route("admin/client/list/register/try")
# def admin_register_try():
#   ok = admin.new_admin(request.form)
#   if not ok: return redirect("/admin/client/list/register")
#   return redirect("admin/client/list/secret")


if __name__ == "__main__":
  app.run(debug=True)