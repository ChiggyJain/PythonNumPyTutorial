import pandas as pd
import numpy as np
from fastapi import FastAPI

df = pd.DataFrame({
    'marks': [50, 60, 70, 80],
    'subjects': ["S1", "S2", "S3", "S4"],
})
print(f"df: {df}")
print(f"type(df['marks'].values): {type(df['marks'].values)}")
print("\nConvert Pandas → NumPy")
print(f"df['marks'].to_numpy(): {df['marks'].to_numpy()}")
print(f"df.to_numpy(): {df.to_numpy()}")
print("Convert NumPy → Pandas")
arr = np.array([10,20,30,40])
print(f"pd.DataFrame(arr, columns=['Marks']): {pd.DataFrame(arr, columns=['Marks'])}")
print("\nUse NumPy inside Pandas operations")
df = pd.DataFrame({
    'price': [50, 60, 70, 80]
})
df["final_price"] = df["price"] + np.array([10])
print(f"df: {df}")
print("\nApply NumPy vectorization on DataFrame columns")
df = pd.DataFrame({
    'math': [70,80,90],
    'science': [65,75,85],
    'english': [60,70,80]
})
print(f"df: {df}")
print(f"df.to_numpy(): {df.to_numpy()}")
df["total"] = df[["math", "science", "english"]].to_numpy().sum(axis=1)
df["percent"] = df["total"] / 3
print(f"df: {df}")


scores = {
  "math": [50, 60, 70],
  "science": [45, 55, 65],
  "english": [48, 58, 68]
}
for subject, values in scores.items():
    print(f"Subject: {subject}, Avg-Marks-From-All-Students: {np.array(values).mean()}")


app = FastAPI()
@app.post("/calculate-kpi")
def calculate_kpi(values: list[int]):
    arr = np.array(values)
    
    response = {
        "sum": int(arr.sum()),
        "mean": float(arr.mean()),
        "min": int(arr.min()),
        "max": int(arr.max()),
        "p90": float(np.percentile(arr, 90))
    }
    return response
@app.post("/add-bonus")
def add_bonus(marks: list[int], bonus: int):
    arr = np.array(marks)
    return (arr + bonus).tolist()



