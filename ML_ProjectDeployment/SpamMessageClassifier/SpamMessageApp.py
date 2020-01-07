from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('SpamMessageClsModel.pkl', 'rb'))
cv = pickle.load(open('transform.pkl', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def index():    
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        inputMsg = request.form['message']
        data = [inputMsg]
        cv_X = cv.transform(data).toarray()
        pred = model.predict(cv_X)
    return render_template('result.html', prediction = pred)


if __name__ == "__main__":
    app.run(debug=True)