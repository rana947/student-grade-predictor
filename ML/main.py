import pickle
import numpy as np

# Model load karo
model = pickle.load(open(
    r'C:\Users\FLH\New folder\studentgradepredictor\grade_model.pkl','rb'))

# Naye student ki details daalo
attendance = int(input("Attendance %: "))
sessional = int(input("sessional marks: "))
midterm = int(input("Midterm marks: "))
final = int(input("Final marks: "))

# Predict karo
prediction = model.predict([[attendance, sessional, midterm, final]])
print(f"🎓 Predicted Grade: {prediction[0]}")