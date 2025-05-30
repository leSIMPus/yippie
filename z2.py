import pandas as pd

df = pd.read_csv("students.csv")
df.columns = df.columns.str.strip()

print("Студенты с баллом выше 80:")
high_scores = df[df["Score"] > 80]
print(high_scores.sort_values(by="Score", ascending=False), "\n")

oldest = df[df["Age"] == df["Age"].max()]
youngest = df[df["Age"] == df["Age"].min()]
print("Самый старший студент:")
print(oldest)
print("\nСамый младший студент:")
print(youngest)