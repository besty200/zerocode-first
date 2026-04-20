import pandas as pd


df = pd.read_csv('student_lifestyle_performance_dataset.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df[['Age', 'Branch']])

df1 = pd.read_csv('dz.csv')
print(df1.head())
print(df1.info())
print(df1.describe())
group = df1.groupby('City')['Salary'].mean()
print(group)
