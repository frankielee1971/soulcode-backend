

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# main.py
"""
Main entry point for the SoulCode backend server.
"""

from fastapi import FastAPI
from webhook_receiver.router import router as webhook_router  # 👈 direct import of APIRouter

app = FastAPI()

# Register webhook endpoint
app.include_router(webhook_router)

# Root route for health check
@app.get("/")
def read_root():
    return {"message": "SoulCode portal is alive and sovereign"}
if __name__ == "__main__":
    import os
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)




