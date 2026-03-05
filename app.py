from flask import Flask, render_template, redirect, url_for
from models import db, User
from forms import RegistrationForm
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        # hash password before storing
        hashed_password = generate_password_hash(form.password.data)

        user = User(
            name=form.name.data,
            email=form.email.data,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("success", name=form.name.data))

    return render_template("register.html", form=form)


@app.route("/success/<name>")
def success(name):
    return render_template("success.html", name=name)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)