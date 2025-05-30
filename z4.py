import pandas as pd

df = pd.read_csv("students.csv")
df.columns = df.columns.str.strip()

df["Passed"] = (df["Score"] >= 60).astype(int)

grouped = df.groupby("Group").agg({
    "Score": "mean",
    "Age": "median"
}).rename(columns={"Score": "Средний балл", "Age": "Медианный возраст"})

print("Группировка:")
print(grouped.round(2))

print("Обновленная таблица:")
print(df[["Name", "Score", "Passed"]])