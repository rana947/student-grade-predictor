# Python ka lightweight base image use kar rahe hain
FROM python:3.11-slim

# Container ke andar working directory set karo
WORKDIR /app

# Pehle requirements copy karo (isse Docker layer caching better hoti hai)
COPY requirements.txt .

# Dependencies install karo
RUN pip install --no-cache-dir -r requirements.txt

# Ab poora project copy karo (train.py, students.csv, etc.)
COPY . .

# Jab container run ho, ye command chale
CMD ["python", "train.py"]
