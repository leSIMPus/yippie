import pandas as pd

df = pd.read_csv("students.csv")
df.columns = df.columns.str.strip()

print(df.isnull().sum(), "\n")

df["Score"] = df["Score"].fillna(df["Score"].mean())

df = df.dropna(subset=["Group"])

print("Обновлённые данные:")
print(df)