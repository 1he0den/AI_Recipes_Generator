from openai import AsyncOpenAI # type: ignore
import re
from app.utils.config import settings

client = AsyncOpenAI(api_key=settings.openai_api_key)

class AIService:
    @staticmethod
    async def generate_recipe(prompt: str) -> dict:
        response = await client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """Ты шеф-повар. Формат ответа:
                    Название: [название]
                    Время: [XX] минут
                    Сложность: [легкая|средняя|сложная]
                    Ингредиенты:
                    - [ингредиент 1]
                    - [ингредиент 2]
                    Шаги:
                    1. [шаг 1]
                    2. [шаг 2]"""
                },
                {"role": "user", "content": prompt}
            ]
        )
        return parse_recipe(response.choices[0].message.content)
    @staticmethod
    async def generate_recipe_image(title: str) -> str:
        response = await client.images.generate(
            model="dall-e-3",
            prompt=f"Appetizing {title}, professional food photography, 4K",
            size="1024x1024",
            quality="standard"
        )
        return response.data[0].url

def parse_recipe(text: str) -> dict:
    """Парсит структурированный ответ от GPT"""
    return {
        "title": re.search(r"Название: (.+)", text).group(1),
        "cooking_time": int(re.search(r"Время: (\d+)", text).group(1)),
        "difficulty": re.search(r"Сложность: (.+)", text).group(1),
        "ingredients": re.findall(r"- (.+)", text),
        "instructions": re.findall(r"\d+\. (.+)", text)
    }