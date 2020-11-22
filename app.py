from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.secret_key = "blublunomi_gomugomu"

@app.route("/")
def index():
  return render_template("layout.html")

@app.route("/concept")
def concept():
  return render_template("concept.html")

@app.route("/service")
def service():
  return render_template("service.html")

@app.route("/aboutus")
def aboutus():
  return render_template("aboutus.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

if __name__ == "__main__":
  app.run(debug=True)