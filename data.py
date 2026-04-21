import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('student-mat.csv', sep=';')
print("First 5 rows of the dataset:")
print(df.head)
print("\nMissing values")
print(df.isnull().sum())

df=df.dropna()
df=df.drop_duplicates()

print("\nDataset shape:", df.shape)
print("\nData Types:\n", df.dtypes)

avg_grade=df['G3'].mean()
print("\nAverage Final Grade(G3):", avg_grade)

above_15=df[df['G3']>15]
print("Number of students scoring above 15:", above_15.shape[0])

correlation=df['studytime'].corr(df['G3'])
print("correalation between study time and G3:", correlation)

print("\nAverage Grade by gender:")
print(df.groupby('sex')['G3'].mean())
plt.figure()
plt.hist(df['G3'])
plt.title("Distribution of final grades(G3)")
plt.xlabel("Grades")
plt.ylabel("Frequency")
plt.show()
plt.figure()
plt.scatter(df['studytime'],df['G3'])
plt.title("Study time vs Final grade")
plt.xlabel("Study Time")
plt.ylabel("G3")
plt.show()

plt.figure()
gender_avg.plot(kind='bar')
plt.title("Average score by gender")
plt.xlabel("Gender")
plt.ylabel("Average G3")
plt.show()

import seaborn as sns
plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("correlation Heatmap")
plt.show()

print("n\=====FINAL SUMMARY=======")
print("AVERAGE G3:",avg_grade)
print("students scoring above 15:",above_15.shape[0])
print("studytime vs G3 correlation:", correlation)

if gender_avg['F']>gender_avg['M']:
    print("Female Students perform better on average")
else:
    print("male students perform better on average")
