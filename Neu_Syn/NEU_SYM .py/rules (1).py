def explain_prediction(prediction):
    if prediction == 0:
        return "Traffic is classified as BENIGN. No suspicious attack pattern detected."
    else:
        return "Traffic is classified as ATTACK. Suspicious network behaviour detected."