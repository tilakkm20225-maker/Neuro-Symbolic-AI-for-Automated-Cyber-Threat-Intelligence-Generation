import pandas as pd

file_path = "data/MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"

df = pd.read_csv(file_path)

print("Original Shape:", df.shape)

# remove spaces from column names
df.columns = df.columns.str.strip()

# convert Label to numeric
df['Label'] = df['Label'].apply(lambda x: 0 if x == "BENIGN" else 1)

# drop rows with infinity / null
df = df.replace([float('inf'), -float('inf')], pd.NA)
df = df.dropna()

print("Cleaned Shape:", df.shape)

# split X and y
X = df.drop('Label', axis=1)
y = df['Label']

# save processed dataset
X['Label'] = y
X.to_csv("results/processed.csv", index=False)

print("✅ Processed dataset saved in results folder")