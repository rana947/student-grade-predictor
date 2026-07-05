import requests

# Flask API ka address
url = "http://127.0.0.1:5000/predict"

# Jo data bhejna hai (apne hisaab se numbers change kar sakte ho)
data = {
    "attendance": 85,
    "sessional": 70,
    "midterm": 75,
    "final": 80
}

# Request bhejo aur result print karo
response = requests.post(url, json=data)
print("Result:", response.json())
