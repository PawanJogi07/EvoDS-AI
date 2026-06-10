from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.health import router as health_router
from routes.upload import router as upload_router
from routes.eda import router as eda_router
from routes.automl import router as automl_router
from routes.feature import router as feature_router
from routes.predict import router as predict_router
from routes.train import router as train_router
from routes.model_info import router as model_info_router
from fastapi.staticfiles import StaticFiles
app = FastAPI(
    title="EvoDS AI",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
        "https://evo-ds-ai.vercel.app",
        "https://evo-ds-appqzsw08-pawanjogi07s-projects.vercel.app",
        "https://evo-ds-hs6rd6qdp-pawanjogi07s-projects.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(health_router)
app.include_router(upload_router)
app.include_router(eda_router)
app.include_router(automl_router)
app.include_router(feature_router)
app.include_router(predict_router)
app.include_router(train_router)
app.include_router(model_info_router)

app.mount(
    "/reports",
    StaticFiles(directory="reports"),
    name="reports"
)


@app.get("/")
def home():
    return {
        "message": "EvoDS AI Backend Running 🚀"
    }
