#!/usr/local/bin/python3

from flask import Flask, render_template, request
import smtplib, mail, client, sql
from mail import USER_NAME_CLIENT, USER_NAME_CONTACT, PASSWORD_CLIENT, PASSWORD_CONTACT
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "blublunomi_gomugomu"

HOST = "om1002.coreserver.jp"
PORT = 465

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
  return messsage("お問い合わせ完了。確認メールをご確認ください。", "/", "ホームに戻る")


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

  if request.files:
    design = request.files['design']
    filename = secure_filename(design.filename)
  else:
    design = None
    filename = "無し"

  file_id = str(sql.exec('INSERT INTO test (company_id, user_id, filename) VALUES (%s, %s, %s)', company_id, user_id, filename))

  attach = client.save_file(filename, design, file_id)
  # if attach[0] == "no file": attach[1] = None

  msg = mail.client_create(attach[0])
  host = HOST
  port = PORT

  smtp = smtplib.SMTP_SSL(host, port)
  smtp.login(USER_NAME_CLIENT, PASSWORD_CLIENT)
  smtp.send_message(msg[0])
  smtp.send_message(msg[1])
  smtp.quit()
  return messsage("広告掲載の申し込み受付完了。当社からのご連絡をお待ちください。", "/", "ホームに戻る")


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

def messsage(msg, link, text):
  return render_template("msg.html", message=msg, at=link, text=text)


if __name__ == "__main__":
  app.run(debug=True)