#!/usr/local/bin/python3
from flask import Flask, render_template, request, redirect
import smtplib, mail, sql
from client import client
from admin import admin

app = Flask(__name__)
app.secret_key = "fkldsjt42u815dsfv"
app.register_blueprint(client)
app.register_blueprint(admin)

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
  return redirect("/finished/contact")


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
@app.route("/finished/<page>")
def message(page):
  if page == "contact":
    return render_template("msg.html", message="お問い合わせ完了。確認用メールをご確認ください。", at="/", text="ホームに戻る")
  elif page == "client":
    return render_template("msg.html", message="広告掲載の申し込み受付完了。当社からのご連絡をお待ちください。", at="/", text="ホームに戻る")
  else:
    return render_template("msg.html", message="エラーが発生しました。", at="/", text="ホームに戻る")

if __name__ == "__main__":
  app.run(debug=True)