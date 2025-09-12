from fastapi import FastAPI

app = FastAPI(title="ThreatIQ API")

@app.get("/health")
def health():
    return {"status": "ok"}
