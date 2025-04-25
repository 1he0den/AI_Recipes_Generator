import httpx # type: ignore
from app.utils.config import settings

class SpoonacularService:
    BASE_URL = "https://api.spoonacular.com/recipes"

    @staticmethod
    async def find_recipes_by_ingredients(ingredients: list[str], number: int = 3):
        params = {
            "ingredients": ",".join(ingredients),
            "number": number,
            "apiKey": settings.spoonacular_api_key
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{SpoonacularService.BASE_URL}/findByIngredients",
                params=params
            )
            return response.json()