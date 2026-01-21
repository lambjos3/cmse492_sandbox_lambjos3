import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Exam1": [78, 85, 90, 88, 76],
    "Exam2": [82, 89, 94, 91, 80],
    "Exam3": [75, 84, 88, 90, 79]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

mean_scores = df[["Exam1", "Exam2", "Exam3"]].mean()
print("\nMean Scores for each exam:")
print(mean_scores)

plt.figure()
mean_scores.plot(kind="bar", color="skyblue")
plt.title("Average Exam Scores")
plt.xlabel("Exam")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("data/mean_scores.png")
plt.close()

print("\nPlot saved to data/mean_scores.png")
