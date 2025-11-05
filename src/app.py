from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Aplikasi Seblak Aman</h1><p>Selamat datang di backend utama! -erik</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
