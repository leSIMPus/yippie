import pandas as pd

df = pd.read_csv("students.csv")
print(df.head())
print(df.info())
print(df.describe())

mean_score = df["Score"].mean()
print(f"Средний балл: {mean_score:.2f}")

group_counts = df["Group"].value_counts()
print("Количество студентов в каждой группе:")
print(group_counts)
