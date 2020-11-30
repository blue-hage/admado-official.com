#!/usr/local/bin/python3

from flask import Flask, render_template, redirect, request
import os

app = Flask(__name__)
app.secret_key = "blublunomi_gomugomu"

@app.route("/")
def index_page():
  return render_template("index.html")

@app.route("/concept")
def concept_page():
  return render_template("concept.html")

@app.route("/service")
def service_page():
  return render_template("service.html")

@app.route("/aboutus")
def aboutus_page():
  return render_template("aboutus.html")

@app.route("/contact")
def contact_page():
  return render_template("contact.html")

@app.route("/client")
def client_page():
  return render_template("client.html")

@app.route("/contact/try")
def contact_try():
  return

if __name__ == "__main__":
  app.run(debug=True)
