import os 
import openai

# Authenticate with the OpenAI API
openai.api_key = os.getenv("SECRET_KEY")

# Define the customer review
review = "I absolutely love this product! It's amazing and has exceeded all my expectations."

response = openai.Completion.create(
  engine="davinci",
  prompt=(f"Please analyze the sentiment of the following customer review: '{review}'."),
  max_tokens=1,
  n=1,
  stop=None,
  temperature=0.7,
)

sentiment_score = response.choices[0].text.strip()
