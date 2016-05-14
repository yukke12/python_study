# -*- coding: utf-8 -*-
"""
 Using SQLAlchemy and Flask get db record.(GET)
"""

from flask import Flask, render_template, abort
from flaski.models import WikiContent

app = Flask(__name__)
app.config['DEBUG'] = True


# 起動されたサーバーの/にアクセスした時の挙動を記述。
# @app.route("/hoge")で記述すれば、http://127.0.0.1:5000/aaでアクセスした時の挙動を記述できる。
@app.route("/")
def hello():
    contents = WikiContent.query.all()
    return render_template("index.html", contents=contents)

#/<title>を指定することで、index.htmlのtitle=content.titleを指定して、
@app.route("/<title>", methods=["GET"])
def show_content(title):
    """
    :param title:modelに対するクエリ文字列
    :return:
    """
    # wikicontentテーブルから、titleでフィルタ(where指定して取得) firstは1行だけ取得するの意味。
    # all()だと、結果を複数リスト形式で取得する。
    content = WikiContent.query.filter_by(title=title).first()
    if content is None:
        abort(404)
    return render_template("show_content.html", content=content)

if __name__ == "__main__":
    # サーバーの起動
    app.run()

