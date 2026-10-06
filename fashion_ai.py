import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=api_key)


def get_fashion_advice(
    occasion,
    gender,
    season,
    style,
    color_preference,
    budget,
    outfit_type
):

    prompt = f"""
You are an AI Fashion Assistant.

Give a short, useful fashion recommendation.

Occasion: {occasion}
Gender: {gender}
Season: {season}
Style: {style}
Color: {color_preference}
Budget: {budget}
Outfit: {outfit_type}

Give:
 👗 Recommended outfit
 🎨 Matching colors
 👟 Footwear
 🎒 Accessories
 💡 Styling tips
 🔄 Alternative outfit

Keep the answer under 250 words.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Gemini Error: {e}"