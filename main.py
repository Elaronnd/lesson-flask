from flask import Flask, render_template, redirect, url_for
from forms import UserForm
from config import Config
from model import db, User

web = Flask(__name__)
web.config.from_object(Config)
db.init_app(app=web)


@web.before_request
def before_request():
    db.create_all()


@web.route("/", methods=["GET", "POST"])
def index():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        db.session.add(User(username=username, email=email))
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("index.html", form=form)


if __name__ == "__main__":
    web.run(host="0.0.0.0", port=8000, debug=True)
