from flask import Flask, request
from flask_cors import CORS, cross_origin
import requests

app = Flask('app')
CORS(app)

@app.route('/', methods=["GET","POST"])
@cross_origin()
def index():
  if request.method == 'POST':
    url = "https://www.google.com/search?q=SEARCH+URL+HERE&hl=en-us&source=lnms&tbm=vid"
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'})
    print(resp.status_code)
    return resp.text
  if request.method == 'GET':
    return "<h1>Hello World!</h1>"
