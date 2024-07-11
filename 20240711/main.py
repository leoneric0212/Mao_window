from flask import Flask, render_template
import data


app = Flask(__name__) #設定這裡是根目錄
@app.route("/")
def index():
    # print(list(map(lambda value:value[0],data.get_areas())))
    areas=[tup[0] for tup in data.get_areas()]
    print(areas)
    return render_template('index.html.jinja', areas=areas)