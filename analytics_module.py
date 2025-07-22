
# Mock-up for analyzing AI dating feedback
def analyze_feedback(feedback_list):
    sentiment_score = sum(1 for f in feedback_list if "awkward" not in f)
    return sentiment_score / len(feedback_list)

feedback = ["funny", "awkward"]
print("User Sentiment Score:", analyze_feedback(feedback))
