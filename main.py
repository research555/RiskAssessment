import pandas as pd
import numpy as np
import seaborn as sb
from functions import DataCleaner

pd.set_option("display.max_rows", 15, "display.max_columns", None)
np.set_printoptions(linewidth=360)
raw_data = pd.read_csv('C:/Users/imran/PycharmProjects/RiskAssessment/credit_risk_dataset.csv')

# # # # CLEAN DATA # # # #

# Remove NaN values, duplicates, and convert categorical data to numerical

print(raw_data.loan_status)

x = DataCleaner(df=raw_data, initial_dtype='object', final_dtype='category')
"""

def draw_axvlines(plt, col):
    mean = df_summary.loc["mean", col]
    q1 = df_summary.loc["25%", col]
    q2 = df_summary.loc["50%", col]
    q3 = df_summary.loc["75%", col]
    plt.axvline(mean, color="g")  # Plotting a line to mark the mean 
    plt.axvline(q1, color="b")  # Plotting a line to mark Q1 
    plt.axvline(q2, color="navy")  # Plotting a line to mark Q2 
    plt.axvline(q3, color="purple")  # Plotting a line to mark Q3
    plt.legend({"Mean": mean, "25%": q1, "50%": q2, "75%": q3})
"""

print(x.describe(exclude='category'))  # remove nominal data from analysis

# data has a some outliers esp in employment length



# is data unbalanced? draw boxplots, maybe do SMOTE

# which model? maybe knn is best

# split stratified and run model and test efficiency

# win nobel prize
