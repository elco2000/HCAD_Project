from flask import Flask, render_template
import joblib
import numpy as np
import sklearn

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/form')
def form():
    try:
        model = joblib.load("Notebooks/Completed_model.pkl")
        test_pred = np.array([2, 5, 6, 0, 1, 0, 1, 0, 1]).reshape(1, -1)
        predicted_burnoutrate = model.predict(test_pred)
        print(predicted_burnoutrate)
        return render_template('form.html', rate=float(predicted_burnoutrate))
    except ValueError:
        return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
