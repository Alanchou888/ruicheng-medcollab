from fastapi import FastAPI
from app.routers import (
    auth,
    feedbacks,
    materials,
    projects,
    upload,
    users,
    versions,
    workspace,
)

app = FastAPI(title="睿程生醫 API", version="0.1.0")

app.include_router(auth.router)
app.include_router(materials.router)
app.include_router(projects.router)
app.include_router(workspace.router)
app.include_router(feedbacks.router)
app.include_router(versions.router)
app.include_router(upload.router)
app.include_router(users.router)


@app.get("/health")
def health():
    return {"status": "ok"}
