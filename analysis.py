
# Import pandas library
# Pandas is used for reading and analyzing datasets (tables like Excel)


import pandas as pd

# Import matplotlib library for data visualization
# pyplot helps to create charts like scatter, bar, line etc.
import matplotlib.pyplot as plt


# Read the CSV dataset file
# pd.read_csv() loads the dataset into a DataFrame (table structure)
data = pd.read_csv("student_lifestyle_dataset.csv")


# Display first 5 rows of the dataset
# head() is used to quickly check the dataset structure
print(data.head())


# Show dataset information
# info() displays column names, data types, and missing values
print(data.info())


# Create a new column called "Productivity"
# This is a calculated metric based on study, sleep, and social hours
data["Productivity"] = (

    # Study hours contribute positively to productivity
    data["Study_Hours_Per_Day"] * 10

    # Sleep hours also improve productivity but with smaller weight
    + data["Sleep_Hours_Per_Day"] * 5

    # Social media hours reduce productivity
    - data["Social_Hours_Per_Day"] * 6
)


# Print first 5 rows again to check the new column
print(data.head())


# ----------- Visualization 1 -----------

# Create a scatter plot
# X-axis → Study Hours
# Y-axis → GPA
plt.scatter(data["Study_Hours_Per_Day"], data["GPA"])

# Label for X-axis
plt.xlabel("Study Hours")

# Label for Y-axis
plt.ylabel("GPA")

# Title of the chart
plt.title("Study Hours vs GPA")


# ----------- Visualization 2 -----------

# Create another scatter plot
# X-axis → Sleep Hours
# Y-axis → Stress Level
plt.scatter(data["Sleep_Hours_Per_Day"], data["Stress_Level"])

# X-axis label
plt.xlabel("Sleep Hours")

# Y-axis label
plt.ylabel("Stress Level")

# Chart title
plt.title("Sleep vs Stress")


# Show all charts on the screen
plt.show()