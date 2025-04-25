from fastapi import APIRouter, HTTPException # type: ignore
from app.services.ai_service import AIService
from app.models.schemas import RecipeRequest, RecipeResponse

router = APIRouter()

@router.post("/generate", response_model=RecipeResponse)
async def generate_recipe(request: RecipeRequest):
    prompt = f"""Придумай рецепт используя: {", ".join(request.ingredients)}.
    Диета: {request.diet or 'не указана'}.
    Кухня: {request.cuisine or 'любая'}."""
    
    try:
        # Получаем текстовый рецепт
        recipe = await AIService.generate_recipe(prompt)
        
        # Генерируем изображение
        recipe["image_url"] = await AIService.generate_recipe_image(recipe["title"])
        
        return recipe
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))