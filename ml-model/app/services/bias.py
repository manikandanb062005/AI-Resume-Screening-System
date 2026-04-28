def detect_bias(text):
    bias_words = ["young", "male", "female", "age", "gender"]

    found = [word for word in bias_words if word in text]

    return {
        "bias_detected": len(found) > 0,
        "bias_words": found
    }