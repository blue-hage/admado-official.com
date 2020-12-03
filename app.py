#!/usr/local/bin/python3

from flask import Flask, render_template, redirect, request
import smtplib, backend

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

@app.route("/contact/try", methods=["POST"])
def contact_try():
  msg = backend.contact_create()
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
  msg = backend.client_create()
  host = HOST
  port = PORT

  smtp = smtplib.SMTP_SSL(host, port)
  smtp.login(USER_NAME, PASSWORD)
  smtp.send_message(msg[0])
  smtp.send_message(msg[1])
  smtp.quit()
  return redirect("/message")


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
