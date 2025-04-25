from fastapi import FastAPI # type: ignore
from app.routers import recipes
from app.utils.config import settings
from fastapi.middleware.cors import CORSMiddleware # type: ignore

app = FastAPI(title="AI Шеф", version="1.0.0")

origins = [
    "http://localhost:5173",  # Адрес Vite-разработки
    "http://127.0.0.1:5173",  # Альтернативный адрес
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

app.include_router(recipes.router, prefix="/recipes")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}