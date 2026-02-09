# Workplace Mental Health Risk Analysis

## 📌 Project Overview
This project analyzes a workplace mental health survey to understand how factors such as **work pressure, sleep hours, and family support** influence employee stress levels and mental health conditions. The goal is to generate meaningful insights that can help organizations design better wellness and support programs.

## 🎯 Objective
- Explore and understand mental health data  
- Perform basic data cleaning  
- Conduct univariate and bivariate analysis  
- Identify key risk factors affecting employee wellbeing  

## 🛠 What I Have Implemented (Current Progress)

### 1. Data Loading
- Loaded survey data using Pandas  
- Inspected dataset shape and columns  

### 2. Data Understanding
- Checked missing values  
- Identified incomplete reporting in mental health condition column  

### 3. Exploratory Analysis
- **Univariate Analysis**
  - Distribution of stress levels  
  - Reported mental health conditions  

- **Bivariate Analysis**
  - Relationship between sleep hours and stress  
  - Relationship between work pressure and stress  

### 4. Key Insights So Far
- Employees with **high stress sleep around 4–5 hours**, while low-stress employees sleep around 7 hours  
- Higher work pressure is strongly associated with higher stress  
- Half of the employees fall under the **high stress** category  
- Anxiety and depression are the most commonly reported conditions  

## 🧰 Tech Stack
- Python  
- Pandas  
- Matplotlib  
- Seaborn  

## 📂 Project Structure
```
workplace-mental-health/
│
├── data/
│   └── mental_health.csv
│
├── src/
│   └── analysis.py
│
├── README.md
└── requirements.txt
```

## 🚀 How to Run

1. Clone the repository
```bash
git clone <your-repo-url>
pip install -r requirements.txt
python src/analysis.py


👩‍💻 Author
Pooja Parashuram Bajantri
Aspiring Data Scientist

