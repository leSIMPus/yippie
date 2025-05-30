import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")
df.columns = df.columns.str.strip()

plt.figure(figsize=(8, 4))
plt.hist(df["Score"], bins=10, color="skyblue", edgecolor="black")
plt.title("Распределение баллов")
plt.xlabel("Балл")
plt.ylabel("Количество студентов")
plt.grid(True)
plt.tight_layout()
plt.show()

group_scores = df.groupby("Group")["Score"].mean()

group_scores.plot(kind="bar", color="salmon", edgecolor="black")
plt.title("Средний балл по группам")
plt.xlabel("Группа")
plt.ylabel("Средний балл")
plt.grid(axis='y')
plt.tight_layout()
plt.show()