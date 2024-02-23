import fastapi
router = fastapi.APIRouter()

@router.get("/sections/{id}")
async def read_section():
    return {"courses": []}