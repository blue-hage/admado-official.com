#!/usr/local/bin/python3

from email.mime.text import MIMEText
from email.utils import formatdate
from flask import Flask, render_template, redirect, request
import smtplib

app = Flask(__name__)
app.secret_key = "blublunomi_gomugomu"

USER_NAME = "contact@admado-official.com"
PASSWORD = "20201202"
HOST = "om1002.coreserver.jp"
PORT = 465
ADMADO_RECIPIENT = "contact-receiver@admado-official.com"

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

def mail_create():
  body1 = "test"
  msg1 = MIMEText(body1, "html")
  msg1["Subject"] = "お問い合わせ完了"
  msg1["From"] = USER_NAME
  msg1["To"] = request.form.get("email")

  body2 = "test"
  msg2 = MIMEText(body2 , "html")
  msg2["Subject"] = "お問い合わせの受付"
  msg2["From"] = USER_NAME
  msg2["To"] = ADMADO_RECIPIENT
  msg = [msg1, msg2]
  return msg

@app.route("/contact/try", methods=["POST"])
def contact_try():
  msg = mail_create()
  host = HOST
  port = PORT

  smtp = smtplib.SMTP_SSL(host, port)
  smtp.login(USER_NAME, PASSWORD)
  smtp.send_message(msg[0])
  smtp.send_message(msg[1])
  smtp.quit()
  return redirect("/message")

# client application page
@app.route("/client")
def client_app_page():
  return render_template("client.html")

@app.route("/client/try", methods=["POST"])
def client_try():
  return message_page("未完成", "/client")


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


# message page
@app.route("/message")
def message_page():
  return render_template("msg.html")

if __name__ == "__main__":
  app.run(debug=True)
