import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/processed.csv")

counts = df["Label"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(counts, labels=["Attack", "Benign"], autopct='%1.1f%%')
plt.title("Attack vs Benign Distribution")
plt.savefig("results/data_distribution.png")
plt.show()

print("Saved as results/data_distribution.png")