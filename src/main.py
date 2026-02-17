"""FastAPI application entry point"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    # Startup
    print(f"Starting {settings.app_name}...")
    print(f"Environment: {settings.environment}")
    print(f"GPU Provider: {settings.gpu_provider}")
    
    yield
    
    # Shutdown
    print("Shutting down...")


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    debug=settings.debug,
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.debug else [],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "app": settings.app_name,
        "environment": settings.environment,
    }


@app.get("/health")
async def health():
    """Detailed health check"""
    return {
        "status": "healthy",
        "gpu_provider": settings.gpu_provider,
        "batch_processing": settings.batch_processing,
    }


# Import and include routers (will be added later)
# from src.api.routes import images, jobs, videos
# app.include_router(images.router, prefix="/api/v1/images", tags=["images"])
# app.include_router(jobs.router, prefix="/api/v1/jobs", tags=["jobs"])
# app.include_router(videos.router, prefix="/api/v1/videos", tags=["videos"])


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "src.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.debug,
    )
