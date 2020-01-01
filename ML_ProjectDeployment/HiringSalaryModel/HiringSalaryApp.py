from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    # Loading the model to predict the result
    model = pickle.load(open('HiringSalaryModel.pkl', 'rb'))

    ind_variables = [int(x) for x in request.form.values()]
    res = model.predict([ind_variables])
    res = round(res[0], 2)

    return render_template('index.html', predicted_text='Predicted employee salary is $ {}'.format(res))


if __name__ == "__main__":
    app.run(debug=True)