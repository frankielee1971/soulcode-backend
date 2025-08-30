from fastapi import APIRouter, HTTPException
from webhook_receiver.models.archetype import ArchetypeData
from webhook_receiver.services.notion_logger import log_to_notion


router = APIRouter()

@router.post("/webhook")
async def receive_webhook(data: ArchetypeData):
    print(f"Received archetype data: {data.dict()}")
    try:
        log_to_notion(
            file_name=data.name,
            archetype=data.archetype,
            element=None,
            notes=f"Email: {data.email}, Timestamp: {data.timestamp}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"status": "success", "message": f"Archetype for {data.name} logged

