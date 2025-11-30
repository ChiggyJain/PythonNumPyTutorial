import pandas as pd
import numpy as np
from fastapi import FastAPI


np.random.seed(42)
marks = np.random.randint(40,101, size=(1000, 5))
subjects = ["Math", "Science", "English", "History", "Economics"]
df = pd.DataFrame(marks, columns=subjects)
print(f"df: {df}")

df["total"] = df.to_numpy().sum(axis=1)
df["percent"] = df["total"] / len(subjects)
def assign_grade(p):
    if p >= 90: return "A+"
    if p >= 75: return "A"
    if p >= 60: return "B"
    return "C"
df["grade_letter"] = np.vectorize(assign_grade)(df["percent"])
print(f"df: {df}")

print("Mean per subject")
allSubLvlMean = df[subjects].to_numpy().mean(axis=0)
print(f"Each-SubLvl-Mean: {allSubLvlMean}")

print("Highest scoring subject")
best_subject_max_marks_indx = allSubLvlMean.argmax()
best_subject_marks = allSubLvlMean[best_subject_max_marks_indx]
print(f"Best-Subject-Mean-Marks: {best_subject_marks}")

print("Top 5% cutoff")
p95_cutoff = np.percentile(df["percent"], 95)
print(f"p95_cutoff: {p95_cutoff}")

print("Identify top performers")
top_students = df[df["percent"]>p95_cutoff]
print(f"top_students: {top_students.head()}")

print("Identify struggling students (bottom 10%)")
p10_cutoff = np.percentile(df["percent"], 10)
print(f"p10_cutoff: {p10_cutoff}")
weak_students = df[df["percent"]>p10_cutoff]
print(f"weak_students: {weak_students.head()}")

print("Student Rank Calculation")
df["rank"] = df["total"].rank(ascending=True, method="dense").astype(int)
print(f"df: {df}")


app = FastAPI()
@app.post("/student-analytics")
def student_analytics():
    response = {
        "best_subject": "",
        "subject_mean": allSubLvlMean.tolist(),
        "top_5_percent_cutoff": float(p95_cutoff),
        "bottom_10_percent_cutoff": float(p10_cutoff)
    }
    return response
