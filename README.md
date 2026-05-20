# Predictive Analytics Using Historical Data

## Project Overview

This project uses Machine Learning techniques to predict student final grades using historical academic data.  
A Linear Regression model is trained using student-related features such as study time, failures, absences, and previous grades.

The project demonstrates:
- Predictive analytics
- Data preprocessing
- Regression modeling
- Model evaluation
- Data visualization

---

# Objective

To build a predictive model that forecasts student final grades based on historical educational data.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- VS Code

---

# Dataset Used

Student Performance Dataset

The dataset contains student-related information such as:
- Study time
- Number of failures
- Absences
- Parent education
- Previous grades
- Lifestyle and social factors

---

# Machine Learning Model

Linear Regression

Regression equation:

\[
y = mx + b
\]

Where:
- y = predicted output
- m = slope
- x = input variable
- b = intercept

---

# Features Used for Prediction

| Feature | Description |
|---|---|
| studytime | Weekly study time |
| failures | Number of past failures |
| absences | Number of absences |
| G1 | First period grade |
| G2 | Second period grade |

### Target Variable
- G3 (Final Grade)

---

# Project Workflow

1. Load historical dataset
2. Clean and preprocess data
3. Select important features
4. Split training and testing data
5. Train Linear Regression model
6. Make predictions
7. Evaluate model accuracy
8. Visualize predictions using graphs

---

# Data Preprocessing

The following preprocessing steps were performed:

- Removed missing values
- Removed duplicate rows
- Selected useful numeric features

---

# Model Evaluation

## Mean Squared Error (MSE)

\[
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2
\]

Lower MSE indicates better prediction accuracy.

---

## R² Score

R² Score measures how well the model predicts the target variable.

- Closer to 1 → Better model
- Closer to 0 → Poor model

---

# Output Screenshots

## 1. Terminal Output

![Terminal Output](screenshots/terminal_output.png)

---

## 2. Actual vs Predicted Grades Scatter Plot

![Scatter Plot](screenshots/scatter_plot.png)

---

## 3. Actual vs Predicted Grades Line Graph

![Line Graph](screenshots/line_graph.png)

---

# Sample Prediction

Example student data:

| studytime | failures | absences | G1 | G2 |
|---|---|---|---|---|
| 3 | 1 | 4 | 12 | 13 |

The trained model predicts the final grade using the above inputs.

---

# Project Structure

```plaintext
PredictiveAnalyticsProject/
│
├── main.py
├── data.csv
├── README.md
│
└── screenshots/
    ├── terminal_output.png
    ├── scatter_plot.png
    └── line_graph.png
```

---

# Future Improvements

- Add advanced machine learning models
- Improve prediction accuracy
- Create Streamlit web application
- Deploy project online
- Add interactive dashboard visualizations

---

# Conclusion

This project successfully demonstrates predictive analytics using historical student data.  
The Linear Regression model predicts student final grades based on academic and behavioral features.

The project helped in understanding:
- Machine Learning workflows
- Regression analysis
- Data preprocessing
- Predictive modeling
- Forecasting techniques
- Data visualization

---