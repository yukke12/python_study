# -*- coding: utf-8 -*-
from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def hello():
    # title='hogehoge'で指定した物は、index.html内で{{}}で囲って展開できる。
    return render_template("index.html", title="Flaski")

if __name__ == "__main__":
    app.run()
