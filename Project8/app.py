import getpass
import json
import os
from datetime import datetime

from cryptography.fernet import Fernet
from flask import Flask, redirect, url_for, render_template, request, session, g, flash
from ip2geotools.databases.noncommercial import DbIpCity

app = Flask(__name__)
app.secret_key = os.urandom(16)

PATH = "{}{}".format(os.getcwd(), "/static/data/data.json")


@app.before_request
def before_request():
    """
    Establish global user_id from session.
    :return:
    """
    if "user_id" in session:
        g.user = session["user_id"]
    else:
        g.user = None


@app.route("/", methods=["GET", "POST"])
def login():
    """
    Checks for valid email/password combo.
    :return: Login page
    """
    if request.method == "POST":
        session.pop("user_id", None)

        email = request.form["email"]
        password = request.form["password"]

        if check_user(email, password):
            return redirect(url_for("splash"))
        else:
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/password-reset", methods=["GET", "POST"])
def reset():
    """
    Attempts to reset account password after performing check.
    :return: Password Reset page
    """
    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        if check_password(password):
            if change_password(email, password):
                session.pop('_flashes', None)
                flash("Password changed successfully.", category="success")
                return redirect(url_for("login"))
            else:
                flash("User does not exist.", category="danger")

    return render_template("password-reset.html")


@app.route("/splash")
def splash():
    """
    Redirects to Splash page after successful authentication.
    :return: Splash page
    """
    return render_template("splash.html")


@app.route("/admin")
def admin():
    """
    Redirects to Login page
    :return: Login page
    """
    return redirect((url_for("login")))


def check_user(email, password):
    """
    Checks if user exists and creates new user if not. Logs failed login
    attempt if password is incorrect and flashes screen.
    :param email:
    :param password:
    :return: Boolean state for user check
    """
    ip_addr = request.environ['REMOTE_ADDR']

    try:
        with open(PATH, "r") as in_file:
            data = json.load(in_file)

        for user in data["USERS"]:
            for key in user.keys():
                if key == email:
                    if handle_password(user[email]["KEY"], user[email]["PASSWORD"], decrypt=True) == password:
                        if not check_logs(ip_addr):
                            session["user_id"] = user[email]["USERNAME"]
                            return True
                    else:
                        check_logs(ip_addr)
                        flash("Your password is incorrect.", category="danger")
                        return False

        flash("User does not exist, attempting to create account.", category="warning")
        create_account(email, password)
    except (KeyError, IOError):
        flash("Cannot communicate with server. Please try again later.", category="danger")
        return False


def handle_password(key, password, decrypt=False):
    """
    Uses generated cipher key to encrypt/decrypt password.
    :param key:
    :param password:
    :param decrypt:
    :return: password in desired format
    """
    if decrypt:
        key = str.encode(key)
        cipher_suite = Fernet(key)
        user_password = str.encode(password)
        ciphered_text = (cipher_suite.decrypt(user_password))
        deciphered_text = bytes.decode(ciphered_text)

        return deciphered_text
    else:
        key = Fernet.generate_key()
        new_password = str.encode(password)
        cipher_suite = Fernet(key)
        ciphered_text = cipher_suite.encrypt(new_password)  # Required to be bytes
        new_password = bytes.decode(ciphered_text)
        cipher_key = bytes.decode(key)

        return cipher_key, new_password


def check_password(password):
    """
    Checks password against NIST SP 800-63B criteria and flashes
    warning to user if password criteria is not met.
    :param password:
    :return: Boolean state for password check
    """
    common_passwords = []

    try:
        with open(PATH, "r") as in_file:
            data = json.load(in_file)

        common_passwords = data["COMMON PASSWORDS"]
    except (KeyError, IOError):
        pass

    if 8 < len(password) > 64:
        flash("Your password must be greater than 7 characters and less than 65.", category="warning")
        return False
    elif password in common_passwords:
        flash("Your password is too common, please try something more complicated.", category="warning")
        return False

    return True


def check_logs(ip_addr):
    """
    Checks logs for login attempts. Locks account if user has more than
    (5) failed login attempts within (5) minutes and flags account with
    geolocation if successful coordinates are obtained.
    :param ip_addr:
    :return: Boolean acc_locked
    """
    date, time = datetime.now().strftime('%Y-%m-%d %H:%M:%S').split()
    acc_locked = False
    ip_found = False

    try:
        with open(PATH, "r") as in_file:
            data = json.load(in_file)

        for log in data["LOGS"]:
            for ip in log.keys():
                if ip == ip_addr:
                    ip_found = True
                    if int(time.replace(":", "")) - int(log[ip]["TIME"].replace(":", "")) > 300:
                        acc_locked = False
                        log[ip].update(ATTEMPT=1, DATE=date, TIME=time, FLAGS="")
                    else:
                        log[ip]["ATTEMPT"] += 1
                        log[ip].update(DATE=date, TIME=time)
                        if log[ip]["ATTEMPT"] > 5:
                            acc_locked = True
                            flash("Too many login attempts. Please wait 5 minutes and try again.", category="warning")
                            flag = DbIpCity.get('147.229.2.90', api_key='free')  # Placeholder ip_addr
                            flag = flag if flag else "(Unable to obtain location)"
                            log[ip].update(FLAGS=f"{ip_addr} had {log[ip]['ATTEMPT']} failed login attempts within 5 "
                                                 f"minutes on {date} from LAT/LONG: {flag.latitude, flag.longitude}.")

        if not ip_found:
            data["LOGS"].append({ip_addr: {"ATTEMPT": 1, "DATE": date, "TIME": time, "FLAGS": ""}})

        with open(PATH, "w") as out_file:
            json.dump(data, out_file, indent=4, sort_keys=True)
    except (KeyError, IOError):
        pass

    return acc_locked


def create_account(email, password):
    """
    Creates new account from supplied email/password then change password
    for encrypted set. Prompts user if errors occur.
    :param email:
    :param password:
    :return: Boolean state for account creation
    """
    session.pop('_flashes', None)

    try:
        with open(PATH, "r") as in_file:
            data = json.load(in_file)

        data["USERS"].append({email: {"KEY": "", "PASSWORD": "", "USERNAME": getpass.getuser()}})

        with open(PATH, "w") as out_file:
            json.dump(data, out_file, indent=4, sort_keys=True)
    except(KeyError, IOError, PermissionError):
        flash("Unable to create new account.", category="danger")
        return False

    change_password(email, password)
    flash("New account created successfully.", category="success")

    return True


def change_password(email, password):
    """
    Changes password after encrypting supplied password.
    :param email:
    :param password:
    :return: Boolean state for password change
    """
    try:
        with open(PATH, "r") as in_file:
            data = json.load(in_file)

        for user in data["USERS"]:
            for key in user.keys():
                if key == email:
                    cipher_key, new_password = handle_password(None, password)
                    user[key].update(KEY=cipher_key, PASSWORD=new_password)

                    with open(PATH, "w") as out_file:
                        json.dump(data, out_file, indent=4, sort_keys=True)
                    return True
        return False
    except (KeyError, IOError):
        flash("Unable to change password.", category="danger")


if __name__ == "__main__":
    app.run()
