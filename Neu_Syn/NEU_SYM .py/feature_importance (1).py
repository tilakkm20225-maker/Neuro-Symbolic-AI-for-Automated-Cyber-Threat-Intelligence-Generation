import pandas as pd
import matplotlib.pyplot as plt
import joblib

# load processed dataset
df = pd.read_csv("results/processed.csv")

X = df.drop("Label", axis=1)

# load trained model
model = joblib.load("results/random_forest_model.pkl")

# get feature importance
importances = model.feature_importances_

feature_names = X.columns

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importances
})

importance_df = importance_df.sort_values(by="Importance", ascending=False).head(15)

plt.figure(figsize=(10,6))
plt.barh(importance_df["Feature"], importance_df["Importance"])
plt.title("Top Feature Importance")
plt.gca().invert_yaxis()

plt.savefig("results/feature_importance.png")
plt.show()