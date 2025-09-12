from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth  # NEW

app = FastAPI(title="ThreatIQ API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)  # NEW

@app.get("/health")
def health():
    return {"status": "ok"}
