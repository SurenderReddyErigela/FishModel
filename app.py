from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
with open('fish_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/predict', methods=['POST'])
def predict():
    species = request.form.get('species')
    length1 = float(request.form.get('length1'))
    length2 = float(request.form.get('length2'))
    length3 = float(request.form.get('length3'))
    height = float(request.form.get('height'))
    width = float(request.form.get('width'))

    # Create a DataFrame for the input data
    input_data = pd.DataFrame({
        'Species': [species],
        'Length1': [length1],
        'Length2': [length2],
        'Length3': [length3],
        'Height': [height],
        'Width': [width]
    })

    # Make a prediction
    prediction = model.predict(input_data)

    return render_template('results.html', prediction=round(prediction[0], 2))

if __name__ == '__main__':
    # Use PORT environment variable if available, otherwise default to 5000.
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)