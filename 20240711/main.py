from flask import Flask, render_template

app = Flask(__name__) #設定這裡是根目錄
@app.route("/")
def index():
    content='可以在<strong>這邊</strong>顯示內容'
    return render_template('index.html.jinja',left=content)