from pydantic import BaseModel, HttpUrl # type: ignore
from typing import List, Optional

class RecipeRequest(BaseModel):
    ingredients: List[str]
    diet: Optional[str] = None  # Делаем поле необязательным
    cuisine: Optional[str] = None


class RecipeResponse(BaseModel):
    title: str
    ingredients: list[str]
    instructions: list[str]  # Теперь список шагов
    cooking_time: int        # В минутах
    difficulty: str          # "легкая", "средняя", "сложная"
    image_url: HttpUrl | None = None