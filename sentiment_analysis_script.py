#import openai_secret_manager
import openai

# Authenticate with the OpenAI API
#secrets = openai_secret_manager.get_secret("openai")
openai.api_key = "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"

# Define the customer review
review = "I absolutely love this product! It's amazing and has exceeded all my expectations."

# Call the OpenAI Sentiment Analysis PAID API
# response = openai.Completion.create(
#   engine="davinci",
#   prompt=(f"Please analyze the sentiment of the following customer review: '{review}'."),
#   max_tokens=1,
#   n=1,
#   stop=None,
#   temperature=0.7,
# )

# Extract the sentiment score from the API response
# sentiment_score = response.choices[0].text.strip()

# # Print the sentiment score
# print("The sentiment of the customer review is:", sentiment_score)




##### Free Version ####


def analyze_sentiment(review):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Sentiment analysis of customer review: {review}\n",
        temperature=0.5,
        max_tokens=1,
        n=1,
        stop=None,
        timeout=1500,
    )

    sentiment = response.choices[0].text.strip().lower()
    if sentiment == "positive":
        return 1
    elif sentiment == "negative":
        return -1
    else:
        return 0

sentiment = analyze_sentiment(review)
if sentiment == 1:
    print("The customer review is positive.")
elif sentiment == -1:
    print("The customer review is negative.")
else:
    print("The customer review is neutral.")
