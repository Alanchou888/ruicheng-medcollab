from fastapi import FastAPI

app = FastAPI(title="睿程生醫 API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}
