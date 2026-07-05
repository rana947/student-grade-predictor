from flask import Flask, request, jsonify
import pickle

# Flask app shuru karo
app = Flask(__name__)

# Pehle se saved model load karo (train.py ne ye file banayi thi)
with open('grade_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Ek route banao - matlab ek address jahan koi data bhej sakta hai
@app.route('/predict', methods=['POST'])
def predict():
    # Jo data bheja gaya hai use nikalo (JSON format mein aayega)
    data = request.get_json()

    attendance = data['attendance']
    sessional = data['sessional']
    midterm = data['midterm']
    final = data['final']

    # Model se prediction lo
    prediction = model.predict([[attendance, sessional, midterm, final]])

    # Result wapis bhejo JSON format mein
    return jsonify({'predicted_grade': str(prediction[0])})

# Ek simple check route - taake pata chale API zinda hai
@app.route('/')
def home():
    return "Grade Predictor API is running!"

# App ko run karo
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
