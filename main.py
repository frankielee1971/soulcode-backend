# main.py
"""
Main entry point for the backend server.
"""

from fastapi import FastAPI
from webhook_receiver.router import router as webhook_router  # 👈 direct import

app = FastAPI()

# Register webhook endpoint
app.include_router(webhook_router)

# Expose root route for health check and JSON response
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "DigitallyDefined FastAPI backend is live."
    }

# Optional: Local dev entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



