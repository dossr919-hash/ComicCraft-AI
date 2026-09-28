from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/generate")
async def generate_comic(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "A cute cat superhero")
        from app.ai.gemini_flash import generate_comic_outline
        try:
            result = await generate_comic_outline(prompt)
            return JSONResponse(content=result)
        except Exception as e:
            print(f"Gemini Error: {e}")
            return JSONResponse(content={
                "title": "Super Cat in Chennai!",
                "panels": [
                    {"id": 1, "text": "A cute cat finds a magic cape in Chennai", "image_prompt": "cute cat with cape"},
                    {"id": 2, "text": "Cat becomes superhero and flies over Marina Beach", "image_prompt": "cat flying over beach"},
                    {"id": 3, "text": "Cat saves the city!", "image_prompt": "superhero cat saving city"}
                ],
                "note": f"Real AI failed, fallback: {str(e)}"
            })
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=200)