from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)

# Path to the directory where your script is located
encoders_path = os.path.dirname(os.path.abspath(__file__))

# Load the model
model = pickle.load(open(os.path.join(encoders_path, 'lgr.pkl'), 'rb'))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return render_template("predict.html")

@app.route('/results', methods=['POST'])
def results():
    if request.method=="POST":
        satisfaction_level=request.form['satisfaction_level']
        last_evaluation=request.form['last_evaluation']
        number_project=request.form['number_project']
        average_monthly_hours=request.form['average_monthly_hours']
        time_spend_company=request.form['time_spend_company']
        work_accident=request.form['Work_accident']
        left=request.form['left']
        promotion_last_5years=request.form['promotion_last_5years']
        salary=request.form['salary']
        
        pred = [[float(satisfaction_level), float(last_evaluation), float(number_project),
                float(average_monthly_hours), float(time_spend_company), float(work_accident),
                float(left), float(promotion_last_5years), float(salary)]]
        
        print(pred)
        output=model.predict(pred)
        print(output)
    return render_template("results.html",predict="Predict the Likelihood of an Employee Leaving The Company:" +str(output[0]))

if __name__ == '__main__':
    app.run(debug=True)
