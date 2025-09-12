import google.generativeai as genai
from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Say hello from Gemini!")
print("Gemini response:", response.text)
