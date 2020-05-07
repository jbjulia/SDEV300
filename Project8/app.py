import json
import os
from datetime import datetime

from cryptography.fernet import Fernet
from flask import Flask, redirect, url_for, render_template, request, session, g, flash

app = Flask(__name__)
app.secret_key = os.urandom(16)

PATH = "{}{}".format(os.getcwd(), "/static/data/data.json")


@app.before_request
def before_request():
    if "user_id" in session:
        g.user = session["user_id"]
    else:
        g.user = None


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.pop("user_id", None)

        email = request.form["email"]
        password = request.form["password"]

        if check_user(email, password):
            return redirect(url_for("splash"))
        else:
            logger(request.environ['REMOTE_ADDR'])
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/password-reset", methods=["GET", "POST"])
def reset():
    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        if check_password(password):
            if change_password(email, password):
                session.pop('_flashes', None)
                flash("Password changed successfully.")
                return redirect(url_for("login"))
            else:
                flash("User does not exist.")

    return render_template("password-reset.html")


@app.route("/splash")
def splash():
    return render_template("splash.html")


@app.route("/admin")
def admin():
    return redirect((url_for("login")))


def check_user(email, password):
    try:
        with open(PATH, "r") as in_file:
            data = json.load(in_file)

        for user in data["USERS"]:
            if email in user.keys():
                if decrypt_password(user[email]["KEY"], user[email]["PASSWORD"]) == password:
                    session["user_id"] = user[email]["USERNAME"]
                    return True
                else:
                    flash("Your password is incorrect.")
                break
            else:
                flash("User does not exist.")
                break
    except (KeyError, IOError):
        flash("Cannot communicate with server. Please try again later.")
        return False


def decrypt_password(key, password):
    key = str.encode(key)
    cipher_suite = Fernet(key)
    user_password = str.encode(password)
    ciphered_text = (cipher_suite.decrypt(user_password))
    deciphered_text = bytes.decode(ciphered_text)

    return deciphered_text


def check_password(password):
    common_passwords = []

    try:
        with open(PATH, "r") as in_file:
            data = json.load(in_file)

        common_passwords = data["COMMON PASSWORDS"]
    except IOError:
        pass

    if 8 < len(password) > 64:
        flash("Your password must be greater than 7 characters and less than 65.")
        return False
    elif password in common_passwords:
        flash("Your password is too common, please try something more complicated.")
        return False

    return True


def logger(ip_addr):
    try:
        with open(PATH, "r") as in_file:
            data = json.load(in_file)

        data["LOGS"].append(f"Failed login attempt from {ip_addr} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")

        with open(PATH, "w") as out_file:
            json.dump(data, out_file, indent=4, sort_keys=True)
    except (KeyError, IOError):
        pass


def change_password(email, password):
    key = Fernet.generate_key()
    new_password = str.encode(password)
    cipher_suite = Fernet(key)
    ciphered_text = cipher_suite.encrypt(new_password)  # Required to be bytes
    new_password = bytes.decode(ciphered_text)
    cipher_key = bytes.decode(key)

    try:
        with open(PATH, "r") as in_file:
            data = json.load(in_file)

        for user in data["USERS"]:
            for key in user.keys():
                if key == email:
                    user[key].update(PASSWORD=new_password)
                    user[key].update(KEY=cipher_key)

                    with open(PATH, "w") as out_file:
                        json.dump(data, out_file, indent=4, sort_keys=True)
                    return True
        return False
    except (KeyError, IOError):
        pass


if __name__ == "__main__":
    app.run()
