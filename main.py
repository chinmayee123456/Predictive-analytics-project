import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# -----------------------------
# LOAD DATASET
# -----------------------------
df = pd.read_csv("data.csv")

# -----------------------------
# DISPLAY FIRST 5 ROWS
# -----------------------------
print("\nFirst 5 Rows:\n")
print(df.head())

# -----------------------------
# DATA CLEANING
# -----------------------------
print("\nChecking Missing Values:\n")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

print("\nDataset Shape After Cleaning:")
print(df.shape)

# -----------------------------
# SELECT FEATURES AND TARGET
# -----------------------------
# Input features
X = df[['studytime', 'failures', 'absences', 'G1', 'G2']]

# Target variable
y = df['G3']

# -----------------------------
# SPLIT DATASET
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# CREATE MODEL
# -----------------------------
model = LinearRegression()

# -----------------------------
# TRAIN MODEL
# -----------------------------
model.fit(X_train, y_train)

print("\nModel Training Completed!")

# -----------------------------
# MAKE PREDICTIONS
# -----------------------------
predictions = model.predict(X_test)

print("\nPredicted Grades:\n")
print(predictions[:10])

# -----------------------------
# MODEL EVALUATION
# -----------------------------
mse = mean_squared_error(y_test, predictions)

r2 = r2_score(y_test, predictions)

print("\nMean Squared Error:", mse)

print("R2 Score:", r2)

# -----------------------------
# PREDICT NEW STUDENT RESULT
# -----------------------------
# studytime, failures, absences, G1, G2
new_student = [[3, 1, 4, 12, 13]]

predicted_grade = model.predict(new_student)

print("\nPredicted Final Grade for New Student:")

print(predicted_grade)

# -----------------------------
# VISUALIZATION 1
# ACTUAL VS PREDICTED
# -----------------------------
plt.scatter(y_test, predictions)

plt.xlabel("Actual Grades")

plt.ylabel("Predicted Grades")

plt.title("Actual vs Predicted Grades")

plt.show()

# -----------------------------
# VISUALIZATION 2
# LINE GRAPH
# -----------------------------
plt.plot(y_test.values[:20], label="Actual")

plt.plot(predictions[:20], label="Predicted")

plt.xlabel("Students")

plt.ylabel("Grades")

plt.title("Actual vs Predicted Grades Comparison")

plt.legend()

plt.show()