import time

from flask import Flask, request, render_template, redirect
from database import init_db
from database import db_session
from models import Wall


app = Flask(__name__)
init_db()


class Comment(object):
    def __init__(self, author, record):
        self.author = author
        self.record = record


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        author = request.form["author"]
        comment = request.form["comment"]

        rec = Wall(author, comment)
        db_session.add(rec)
        db_session.commit()

        return redirect("/comments")

    return render_template("index.html")


@app.route("/comments", methods=["GET"])
def comments():
    authors_and_comments = Wall.query.all()

    wall = []
    for row in authors_and_comments:
        author = row.author
        comment = row.comment
        wall.append(Comment(author, comment))

    return render_template("comments.html", comments=wall)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
