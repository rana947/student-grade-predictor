import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# CSV Direct path - apna username check karo
df = pd.read_csv('students.csv')
print("✅ Data loaded!\n", df)

# Features aur Label
X = df[['attendance', 'sessional', 'midterm', 'final']]
y = df['grade']

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Model train
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

# Model Save - same folder mein
with open('grade_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model saved successfully! Project complete!")