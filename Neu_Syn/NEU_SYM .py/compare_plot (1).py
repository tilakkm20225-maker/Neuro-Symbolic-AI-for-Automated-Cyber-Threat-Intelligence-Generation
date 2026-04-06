import matplotlib.pyplot as plt

models = ["Random Forest", "Logistic Regression", "Decision Tree"]
accuracy = [0.9999, 0.96, 0.9998]  # use your actual values

plt.bar(models, accuracy)
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.savefig("results/model_comparison.png")
plt.show()