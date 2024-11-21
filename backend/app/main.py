from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.routes import router

# Créer une instance FastAPI
app = FastAPI()

# Ajouter un middleware pour gérer CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # Permettre toutes les origines (changez en fonction de vos besoins)
    allow_credentials=True,
    allow_methods=["*"],  # Permettre toutes les méthodes HTTP
    allow_headers=["*"],  # Permettre tous les headers
)


# Middleware pour capturer et logger les exceptions non gérées
@app.middleware("http")
async def log_exceptions(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        print(f"Unhandled exception: {e}")
        return JSONResponse(status_code=500, content={"detail": str(e)})


# Ajouter les routes
app.include_router(router)
