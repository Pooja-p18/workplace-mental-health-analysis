# Workplace Mental Health Analysis
# Author: Pooja Parashuram Bajantri
# Date: 09/02/2026

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
def load_data():
    df = pd.read_csv('data/mental_health.csv')
    return df

# Basic information and missing values
def basic_info(df):
    print("Shape:", df.shape)
    print("Columns:", df.columns)
    print("\nMissing values:\n", df.isnull().sum())

# Data cleaning
def cleaning_data(df):

    # 1. Remove duplicates
    df = df.drop_duplicates()

    # 2. Standardize text columns
    df['gender'] = df['gender'].str.title()
    df['stress_level'] = df['stress_level'].str.title()

    # 3. Convert treatment to numeric for analysis
    df['treatment_flag'] = df['treatment'].map({'Yes': 1, 'No': 0})

    print("\nAfter Cleaning - Shape:", df.shape)
    return df

def univariate_analysis(df):
    print("\n---Univariate Insights---")

    print("\nStress Level Distribution:")
    print(df['stress_level'].value_counts())

    print("\nMental Health Condition:")
    print(df['mental_health_condition'].value_counts())

def bivariate_analysis(df):
    print("\n---Bivariate Insights---")

    # Average sleep by by stress level
    sleep_stress = df.groupby('stress_level')['sleep_hours'].mean()
    print("\nAverage sleep hours by stress level:")
    print(sleep_stress)

    # Work pressure vs stress
    wp = df.groupby('stress_level')['work_pressure'].mean()
    print("\nAvg Work Pressure By Stress Level:")
    print(wp)

if __name__ == "__main__":
    data = load_data()
    basic_info(data)

    data = cleaning_data(data)

    univariate_analysis(data)
    bivariate_analysis(data)

