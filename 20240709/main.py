from flask import Flask , render_template

appp = Flask(__name__)

# @appp.route("/")
# def myfunc1():
#     return "<h2>我的主題</h2>\n<p>這三小</p>"

# @appp.route("/hello")
# def hello():
#     return "<h3>Hellllooooo</h3>"

# @appp.route("/user/<username>")
# def show_user_profile(username):
#     return f"<h3>嗨嗨{username}</h3>"

# @appp.route("/post/<int:post_id>")
# def post(post_id):
#     return f"<h1>Post  {post_id}</h1>"

@appp.route("/")
def index():
    return render_template('index.html.jinja')

@appp.route("/new")
def new():
    return render_template('new.html.jinja')

@appp.route("/youbike")
def youbike():
    return render_template('youbike.html.jinja')

@appp.route("/contact")
def contact():
    return render_template('contact.html.jinja')
