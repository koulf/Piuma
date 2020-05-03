from flask import Flask, request, send_from_directory
import os
import socket

app = Flask(__name__, static_url_path='')

@app.route("/")
def hello():
    html = open("index.html", 'r').read()
    return html

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)

if(__name__ == "__main__"):
    app.run(host='0.0.0.0',port=80)