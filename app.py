from flask import Flask, render_template, request
import joblib
import numpy as np
from forms import BurnoutForm
import os
import sklearn

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/form', methods=["GET"])
def form():
    burnout_form = BurnoutForm()
    try:
        model = joblib.load("Notebooks/Completed_model.pkl")
        test_pred = np.array([2, 5, 6, 0, 1, 0, 1, 0, 1]).reshape(1, -1)
        predicted_burnoutrate = model.predict(test_pred)
        print(predicted_burnoutrate)
        return render_template('form.html', rate=float(predicted_burnoutrate), form=burnout_form)
    except ValueError:
        return render_template('index.html')


@app.route('/form', methods=["POST"])
def result():
    try:
        form = request.form
        model = joblib.load("Notebooks/Completed_model.pkl")
        if form['gender'] == "Male":
            gender_male = 1
            gender_female = 0
        else:
            gender_female = 1
            gender_male = 0
        if form['bedrijfstype'] == "Productie":
            productie = 1
            service = 0
        else:
            service = 1
            productie = 0
        if form['thuiswerken'] == "Ja":
            thuiswerken_ja = 1
            thuiswerken_nee = 0
        else:
            thuiswerken_nee = 1
            thuiswerken_ja = 0
        pred = np.array(
            [float(form['hbw']), float(form['wu']), float(form['mo']), gender_female, gender_male, productie, service,
             thuiswerken_nee, thuiswerken_ja]).reshape(1, -1)
        predicted = model.predict(pred)
        print(float(form['hbw']))
        print(float(form['wu']))
        print(float(form['mo']))
        if predicted < 0.2:
            message_conclusion = "Zeer laag"
        elif predicted < 0.4:
            message_conclusion = "Laag"
        elif predicted < 0.6:
            message_conclusion = "Gemiddeld"
        elif predicted < 0.8:
            message_conclusion = "Hoog"
        else:
            message_conclusion = "Zeer hoog"
        return render_template("result.html", rate=float(predicted), message=message_conclusion)
    except ValueError:
        return render_template("form.html")


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
