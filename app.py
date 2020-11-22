from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.secret_key = "blublunomi_gomugomu"

@app.route("/")
def index():
  return render_template("layout.html")

if __name__ == "__main__":
  app.run(debug=True)