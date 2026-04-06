import pandas as pd
import joblib
from rules import explain_prediction

model = joblib.load("results/random_forest_model.pkl")
df = pd.read_csv("results/processed.csv")

# take random sample
sample = df.sample(1).drop("Label", axis=1)

prediction = model.predict(sample)[0]
probability = model.predict_proba(sample)[0][1]

if prediction == 0:
    print("Prediction: BENIGN")
else:
    print("Prediction: ATTACK")

print("Confidence:", probability)
print("Explanation:", explain_prediction(prediction))