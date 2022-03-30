from flask import Flask, request
import os
app = Flask('app', static_url_path="")
@app.route('/', methods=["GET","POST"])
def index():
  if request.method == 'POST':
    os.system("curl " + request.form["url"] + " > temp")
    out = open("temp").read()
    open("temp", "w").close()
    return out
  if request.method == 'GET':
    return "<h1>Hello World!</h1>"
