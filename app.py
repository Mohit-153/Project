import pandas as pd
df = pd.read_csv("students.csv")
print(df.head(10))

x = df.drop("Age",axis=1)
y = df["Age"]

x = pd.get_dummies(x)

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(
x,
y,
test_size=0.20,
random_state=42
)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)

model.fit(x_train,y_train)
y_pred = model.predict(x_test)

print("Actual:")
print(y_test.head(10))

print("Predicted")
print(y_pred[:10])

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='weighted'))
print("Recall:", recall_score(y_test, y_pred, average='weighted'))
print("F1 Score:", f1_score(y_test, y_pred, average='weighted'))

print(classification_report(y_test, y_pred))
import joblib

joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(x.columns.tolist(), "columns.pkl")

print("Saved successfully")
import joblib
import pandas as pd
import numpy as np

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")
scaler = joblib.load("scaler.pkl")

sample = pd.DataFrame({
    "Age":[18],
    "math":[56],
    "science":[35],
    "english":[56],
    })
sample = pd.get_dummies(sample)
sample = sample.reindex(columns=columns,fill_value=0)
prediction = model.predict(sample)

if prediction[0] == 1:
   print("intelligent : yes")
else:
    print("intelligent : No")
    
    
    
    
import streamlit as st 
import pandas as pd
import joblib

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

st.title(" Student iq level Prediction")
age = st.number_input("Age", 10, 30, 18)
gender = st.selectbox("Gender", ["Male", "Female"])

sex = st.selectbox("Sex",["M","F"])

Books = st.selectbox("Student intelligence",
                     ["math","science","english"])

study_hours = st.number_input(
    "Study Hours Per Day",
    0.0, 24.0, 5.0
)

sleep_hours = st.number_input(
    "Sleep Hours Per Day",
    0.0, 24.0, 7.0
)

attendance = st.number_input(
    "Attendance Percentage",
    0.0, 100.0, 75.0
)

previous_score = st.number_input(
    "Previous Exam Score",
    0.0, 100.0, 60.0
)

reading_hours = st.number_input(
    "Reading Hours Per Day",
    0.0, 24.0, 2.0
)

screen_time = st.number_input(
    "Screen Time Per Day",
    0.0, 24.0, 3.0
)

extracurricular = st.selectbox(
    "Extracurricular Activities",
    ["Yes", "No"]
)

internet = st.selectbox(
    "Internet Access",
    ["Yes", "No"]
)

predict = st.button("Predict")


if predict:

    input_data = pd.DataFrame({

        "Age": [age],

        "Gender": [gender],

        "StudyHours": [study_hours],

        "SleepHours": [sleep_hours],

        "Attendance": [attendance],

        "PreviousScore": [previous_score],

        "ReadingHours": [reading_hours],

        "ScreenTime": [screen_time],

        "Extracurricular": [extracurricular],

        "InternetAccess": [internet]

    })

    # One-Hot Encoding
    input_data = pd.get_dummies(input_data)

    # Match Training Columns
    input_data = input_data.reindex(
        columns=columns,
        fill_value=0
    )

    # Prediction
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Student Intelligence: HIGH")
    else:
        st.error("Student Intelligence: LOW")
        
        
        
import pandas as pd
df = pd.read_csv("students.csv")
print(df.head(10))

x = df.drop("Age",axis=1)
y = df["Age"]

x = pd.get_dummies(x)

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(
x,
y,
test_size=0.20,
random_state=42
)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)

model.fit(x_train,y_train)
y_pred = model.predict(x_test)

print("Actual:")
print(y_test.head(10))

print("Predicted")
print(y_pred[:10])

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='weighted'))
print("Recall:", recall_score(y_test, y_pred, average='weighted'))
print("F1 Score:", f1_score(y_test, y_pred, average='weighted'))

print(classification_report(y_test, y_pred))
import joblib

joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(x.columns.tolist(), "columns.pkl")

print("Saved successfully")
import joblib
import pandas as pd
import numpy as np

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")
scaler = joblib.load("scaler.pkl")

sample = pd.DataFrame({
    "Age":[18],
    "math":[56],
    "science":[35],
    "english":[56],
    })
sample = pd.get_dummies(sample)
sample = sample.reindex(columns=columns,fill_value=0)
prediction = model.predict(sample)

if prediction[0] == 1:
   print("intelligent : yes")
else:
    print("intelligent : No")
    
    
    
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

st.title(" Student iq level Prediction")
age = st.number_input("Age", 10, 30, 18)
gender = st.selectbox("Gender", ["Male", "Female"])

sex = st.selectbox("Sex",["M","F"])

Books = st.selectbox("Student intelligence",
                     ["math","science","english"])

study_hours = st.number_input(
    "Study Hours Per Day",
    0.0, 24.0, 5.0
)

sleep_hours = st.number_input(
    "Sleep Hours Per Day",
    0.0, 24.0, 7.0
)

attendance = st.number_input(
    "Attendance Percentage",
    0.0, 100.0, 75.0
)

previous_score = st.number_input(
    "Previous Exam Score",
    0.0, 100.0, 60.0
)

reading_hours = st.number_input(
    "Reading Hours Per Day",
    0.0, 24.0, 2.0
)

screen_time = st.number_input(
    "Screen Time Per Day",
    0.0, 24.0, 3.0
)

extracurricular = st.selectbox(
    "Extracurricular Activities",
    ["Yes", "No"]
)

internet = st.selectbox(
    "Internet Access",
    ["Yes", "No"]
)

predict = st.button("Predict")


if predict:

    input_data = pd.DataFrame({

        "Age": [age],

        "Gender": [gender],

        "StudyHours": [study_hours],

        "SleepHours": [sleep_hours],

        "Attendance": [attendance],

        "PreviousScore": [previous_score],

        "ReadingHours": [reading_hours],

        "ScreenTime": [screen_time],

        "Extracurricular": [extracurricular],

        "InternetAccess": [internet]

    })

    # One-Hot Encoding
    input_data = pd.get_dummies(input_data)

    # Match Training Columns
    input_data = input_data.reindex(
        columns=columns,
        fill_value=0
    )

    # Prediction
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Student Intelligence: HIGH")
    else:
        st.error("Student Intelligence: LOW")    
