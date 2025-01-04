# Bike Sharing Demand Prediction
This project is designed to predict bike-sharing demand based on various environmental and weather-related factors. It uses a machine learning model to make predictions, with a frontend built in HTML and a Flask-based backend.

Project Structure
bash
Copy code
/your-repository
├── /client        # Contains index.html (Frontend)
├── /server        # Contains server.py (Flask Backend) and Pre-trained model used for predictions
├── /server        # Contains the dataset and the machine learning algo used
Frontend
The frontend consists of a simple HTML form where users can enter various parameters (such as temperature, humidity, and hour of the day) to predict bike-sharing demand. The data is sent to the Flask backend for prediction.

Backend
The backend is implemented using Flask and serves a prediction API. It loads a pre-trained model (model.pkl) and uses it to predict bike-sharing demand based on the input data.

How to Run
Prerequisites
Install Python 3.x (if not already installed).
Install required Python packages:
bash
Copy code
pip install flask flask-cors numpy scikit-learn
Running the Backend
Navigate to the folder containing server.py.
Start the Flask server by running:
bash
Copy code
python server.py
Open the Frontend
Open index.html in your browser.
Fill in the input fields (holiday, working day, temperature, humidity, etc.) and click Predict to get the bike-sharing demand prediction.
API Endpoint
POST /predict:

Accepts the following JSON payload with input data for prediction:

holiday: 0 or 1
workingday: 0 or 1
atemp: Temperature feeling like
humidity: Humidity level
windspeed: Windspeed
hour: Hour of the day (0-23)
season__1, season__2, season__3, season__4: Binary features for seasons
weather__1, weather__2, weather__3, weather__4: Binary features for weather conditions
Response:

json
Copy code
{
  "predicted_count": 200
}
