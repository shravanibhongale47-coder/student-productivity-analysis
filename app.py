
# Import Streamlit library
# Streamlit is used to create web apps using Python
import streamlit as st

# Import pandas library
# Pandas is used to read and analyze datasets (CSV, Excel etc.)
import pandas as pd

# Import matplotlib for creating graphs
import matplotlib.pyplot as plt


# -------------------------------
# Load Dataset
# -------------------------------

# Read the CSV dataset into a DataFrame
# DataFrame is like a table with rows and columns
data = pd.read_csv("student_lifestyle_dataset.csv")


# -------------------------------
# Title of the Web App
# -------------------------------

# st.title() displays a big heading on the web app
st.title("Student Productivity Predictor")


# -------------------------------
# User Inputs
# -------------------------------

# Slider input for Study Hours
# User can select a value between 0 and 12
study = st.slider("Study Hours", 0, 12)

# Slider input for Sleep Hours
sleep = st.slider("Sleep Hours", 0, 12)

# Slider input for Social Media Hours
social = st.slider("Social Media Hours", 0, 12)


# -------------------------------
# Productivity Formula
# -------------------------------

# Calculate productivity score using a custom formula
# Study increases productivity
# Sleep also increases productivity
# Social media decreases productivity
score = (study * 10) + (sleep * 5) - (social * 6)


# -------------------------------
# Display Productivity Score
# -------------------------------

# Subheading for score section
st.subheader("Productivity Score")

# Display the calculated score
st.write(score)


# -------------------------------
# Productivity Level Classification
# -------------------------------

# If score is less than 40
# Display red error message
if score < 40:
    st.error("Low Productivity ⚠️")

# If score between 40 and 69
# Display yellow warning message
elif score < 70:
    st.warning("Medium Productivity 🙂")

# If score 70 or more
# Display green success message
else:
    st.success("High Productivity 🚀")


# -------------------------------
# Recommendations Section
# -------------------------------

# Section title
st.subheader("Recommendations")


# If social media hours are high
if social > 5:
    st.write("📉 Reduce social media usage")

# If sleep hours are less
if sleep < 6:
    st.write("😴 Increase sleep hours")

# If study hours are less
if study < 4:
    st.write("📚 Increase study time")


# -------------------------------
# Graph 1 : Study Hours vs GPA
# -------------------------------

# Section title
st.subheader("Study Hours vs GPA")

# Create a figure and axis using matplotlib
fig, ax = plt.subplots()

# Scatter plot
# X-axis → Study Hours
# Y-axis → GPA
ax.scatter(data["Study_Hours_Per_Day"], data["GPA"])

# Label X-axis
ax.set_xlabel("Study Hours Per Day")

# Label Y-axis
ax.set_ylabel("GPA")

# Display the chart in Streamlit app
st.pyplot(fig)


# -------------------------------
# Graph 2 : Sleep Hours vs Stress Level
# -------------------------------

# Section title
st.subheader("Sleep Hours vs Stress Level")

# Create another figure
fig2, ax2 = plt.subplots()

# Scatter plot
# X-axis → Sleep Hours
# Y-axis → Stress Level
ax2.scatter(data["Sleep_Hours_Per_Day"], data["Stress_Level"])

# Label X-axis
ax2.set_xlabel("Sleep Hours")

# Label Y-axis
ax2.set_ylabel("Stress Level")

# Show graph in Streamlit
st.pyplot(fig2)