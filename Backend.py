# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import requests

# Create an instance of Flask
app = Flask(__name__)

# Define routes and API endpoints

@app.route('/api/items', methods=['GET'])
def get_items():
    front_end_url="Custom"
    try:
        # Send a GET request to the front end's URL
        response = request.get(front_end_url)
        if response.status_code == 200:
            # The response contains data retrieved from the front end
            data = response.json()  # Assuming the response is in JSON format
            print("Data retrieved from front end:", data)
            prediction(data)
        else:
            print("Request to front end failed with status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        
        print("Request to front end failed:", str(e))

@app.route('/api/items', methods=['POST'])
def prediction(data):
# Load your pre-trained Scikit-Learn model
    model = joblib.load("Final_Classification.pkl") #Final classification will be in here
    try:
    # Get data from the request
        data = request.get_json()
        predictions = model.predict(data)
        return jsonify(predictions.tolist())

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
