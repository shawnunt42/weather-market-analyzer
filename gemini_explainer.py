import os
from google import genai

def make_prediction(city, state, target_date, high_temp, low_temp, threshold):
    try:
        api_key = os.getenv("AIzaSyCwGp2QqmGvweS3yjec8GlxnJdP2XWbAks")

        if not api_key:
            return (
                f"The high will be {high_temp}F and the low will be {low_temp}F. "
                f"The best bet is to bet for the weather to be greater than {threshold}F."
            )

        client = genai.Client(api_key=AIzaSyCwGp2QqmGvweS3yjec8GlxnJdP2XWbAks)

        prompt = f"""
You are a weather prediction assistant.

A user wants a simple weather market style recommendation.

Location: {city}, {state}
Date: {target_date}
Forecasted high: {high_temp}F
Forecasted low: {low_temp}F

Write exactly 2 sentences:
1. State the high and low naturally.
2. Give the best prediction
3. Use a reasonable threshold based on the forecast, and keep it simple.
4. Do not add warnings, disclaimers, or extra explanation.
"""

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception:
        return (
            f"The high will be {high_temp}F and the low will be {low_temp}F. "
            f"The best bet is to bet for the weather to be greater than {threshold}F."
        )