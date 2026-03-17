streamlit run app.py

C:\Users\YourName\Desktop\Student_Productivity_Analysis> streamlit run app.py

Email:

Bas Enter press karo
Email dena zaroori nahi hai.

Uske baad kya hoga

Terminal me kuch aisa dikhega:

Local URL: http://localhost:8501

Example:

Local URL: http://localhost:8501
Network URL: http://192.168.xx.xx:8501



Project: Student Lifestyle and Productivity Analysis
1️⃣ Problem Identify kiya

Sabse pehle humne yeh problem identify ki:

Aajkal students ka study time, sleep aur social media usage unki productivity ko affect karta hai.

Isliye humne ek system banaya jo student lifestyle analyze kare aur productivity calculate kare.

2️⃣ Dataset Use kiya

Humne ek dataset use kiya jisme student lifestyle ki information thi.

Dataset me columns the:

Student_ID

Study_Hours_Per_Day

Sleep_Hours_Per_Day

Social_Hours_Per_Day

Physical_Activity_Hours_Per_Day

GPA

Stress_Level

Is dataset ko Python me load kiya using Pandas.

Example:

data = pd.read_csv("student_lifestyle_dataset.csv")

Is step me humne data ko read aur analyze kiya.

3️⃣ Productivity Formula Banaya

Humne ek formula banaya jo student lifestyle ko use karke productivity score calculate karta hai.

Logic:

Study hours productivity increase karte hain

Sleep hours bhi productivity increase karte hain

Social media productivity decrease karta hai

Formula:

Productivity Score =
(Study Hours × 10) + (Sleep Hours × 5) − (Social Media Hours × 6)

Is formula se system productivity score calculate karta hai.

4️⃣ Productivity Level Classify kiya

Score calculate hone ke baad system usko categories me divide karta hai:

Score	Productivity
0–40	Low Productivity
40–70	Medium Productivity
70+	High Productivity

Isse user ko pata chalta hai ki uski productivity low hai ya high.

5️⃣ Recommendation System Banaya

System user ko suggestions bhi deta hai.

Example:

Agar social media zyada hai → reduce social media

Agar sleep kam hai → increase sleep

Agar study hours kam hai → increase study hours

Isse system student ko better lifestyle suggest karta hai.

6️⃣ Data Visualization kiya

Dataset ko visualize kiya using Matplotlib.

Example graphs:

Study Hours vs GPA

Is graph se pata chalta hai:

Zyada study hours → better academic performance.

Sleep Hours vs Stress Level

Is graph se pata chalta hai:

Kam sleep → stress increase.

Visualization se data patterns samajhne me help milti hai.

7️⃣ Interactive Web Application Banaya

Humne ek web app banaya using Streamlit.

Isme user sliders se input deta hai:

Study Hours

Sleep Hours

Social Media Hours

System instantly:

✔ Productivity score calculate karta hai
✔ Productivity level show karta hai
✔ Recommendations deta hai

8️⃣ Final Dashboard Output

User jab values change karta hai to system:

Productivity score show karta hai

Productivity level batata hai

Lifestyle suggestions deta hai

Dataset graphs display karta hai

Isse project interactive analytics dashboard ban gaya.

9️⃣ Project ka Real Life Use

Ye system students ko help karta hai:

Apni lifestyle habits samajhne me

Productivity improve karne me

Study-life balance maintain karne me

10️⃣ Project se kya seekha

Is project me humne seekha:

Python programming

Data analysis using Pandas

Data visualization using Matplotlib

Interactive dashboard using Streamlit

Real world data analysis