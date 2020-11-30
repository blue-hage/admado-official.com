#!/usr/local/bin/python3

from flask import Flask, render_template, redirect, request
import os

app = Flask(__name__)
app.secret_key = "blublunomi_gomugomu"

# home page
@app.route("/")
def index_page():
  return render_template("index.html")

# concept page
@app.route("/concept")
def concept_page():
  return render_template("concept.html")

# services page
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

# about us page
@app.route("/aboutus")
def aboutus_page():
  return render_template("aboutus.html")

# contact page
@app.route("/contact")
def contact_page():
  return render_template("contact.html")

@app.route("/contact/try")
def contact_try():
  return redirect("/msg")


# client application page
@app.route("/client")
def client_app_page():
  return render_template("client.html")

@app.route("/client/try")
def client_try():
  return render_template("msg.html")


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


if __name__ == "__main__":
  app.run(debug=True)
