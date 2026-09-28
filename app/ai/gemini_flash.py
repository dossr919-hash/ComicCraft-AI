from google import genai
from app.config import settings
import json

client = genai.Client(api_key=settings.gemini_api_key) if settings.gemini_api_key else None

async def generate_comic_outline(prompt: str):
    if not client:
        # Demo data if no API key
        return {
            "title": "Demo Comic",
            "panels": [
                {"panel_number": 1, "description": "Hero entry", "dialogue": "I am here!", "image_prompt": prompt},
                {"panel_number": 2, "description": "Action scene", "dialogue": "Let's go!", "image_prompt": prompt},
            ]
        }
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Create a 4-panel comic outline for: {prompt}. Return ONLY JSON with title and panels array (panel_number, description, dialogue, image_prompt)"
    )
    text = response.text.replace("```json", "").replace("```", "").strip()
    return json.loads(text)