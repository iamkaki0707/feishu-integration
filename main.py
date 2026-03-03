"""
FastAPI Application - Feishu Integration Gateway
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import webhook, messages, calendar, approval
from app.core.config import settings

# Create FastAPI app
app = FastAPI(
    title="Feishu Integration Gateway",
    description="Enterprise integration gateway for Feishu (飞书) - Messages, Calendar, and Approvals",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers
app.include_router(webhook.router, prefix="/api/v1")
app.include_router(messages.router, prefix="/api/v1")
app.include_router(calendar.router, prefix="/api/v1")
app.include_router(approval.router, prefix="/api/v1")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "service": "Feishu Integration Gateway",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "webhook": "/api/v1/webhook",
            "messages": "/api/v1/messages",
            "calendar": "/api/v1/calendar",
            "approval": "/api/v1/approval"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=True
    )
