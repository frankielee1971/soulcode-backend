# main.py
"""
Main entry point for the backend server.
"""
from fastapi import FastAPI
from webhook_receiver import router as webhook_router


app = FastAPI()


# Register webhook endpoint
app.include_router(webhook_router)

# Expose root route for health check and JSON response
@app.get("/")
def root():
    return {"status": "ok", "message": "DigitallyDefined FastAPI backend is live."}

# TODO: Add more routes for agent_tars, generator, etc.

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
