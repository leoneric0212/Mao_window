from flask import Flask , url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>index</h2>'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print("執行test_request_context")
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',name='Mao',password='1234'))
    print(url_for('profile',username='毛'))