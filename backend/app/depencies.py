from fastapi import Depends # type: ignore
from app.services.ai_service import AIService
from app.services.spoonacular_service import SpoonacularService

def get_ai_service():
    return AIService()

def get_spoonacular_service():
    return SpoonacularService()