from email import message
from math import e
from flask import Flask, redirect, render_template, request, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import date

load_dotenv()

app = Flask(__name__)

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app=app)

@app.route("/")
def home():
    with open("static/data/about.txt", "r") as f:
        about = f.readlines()

    with open("static/data/monologue.txt", "r") as f:
        monologue = f.readlines()
    dob = date(1996, 3, 15)
    age = int((date.today() - dob).days / 365.2425)

    skills = pd.read_csv("static/data/skills.csv")
    skills = skills.to_dict(orient='records')
    mid = int(len(skills)/2)
    skills_l = skills[:mid]
    skills_r = skills[mid:]

    success = request.args.get('success')
    error = request.args.get('error')
    return render_template("index.html", about=about, monologue=monologue, age=age, skills_l=skills_l, skills_r=skills_r, success=success, error=error)

@app.route("/send-mail", methods=['GET', 'POST'])
def send_mail():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    msg = Message(subject=subject, sender=app.config['MAIL_USERNAME'], recipients=['jay37tawade@gmail.com'])
    msg.body = f"{name} ({email})\nPosted:\n\n{message}"

    try:
        mail.send(msg)
        return redirect(url_for('home', success=True))
        # return render_template("index.html", success=True, error=None)
    except Exception as e:
        return redirect(url_for("home", error=str(e)))

if __name__ == "__main__":
    app.run(debug=False)