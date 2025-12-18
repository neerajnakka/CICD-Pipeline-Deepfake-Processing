from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import endpoints

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Include V1 Router
app.include_router(endpoints.router, prefix=settings.API_V1_STR)


@app.get("/health")
async def health_check():
    """
    Health check endpoint for the deployment platform.
    """
    return {"status": "healthy", "version": settings.VERSION}


@app.get("/", include_in_schema=False)
async def root():
    """
    Redirect to documentation.
    """
    from fastapi.responses import RedirectResponse

    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
