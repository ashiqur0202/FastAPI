import fastapi
router = fastapi.APIRouter()

@router.get("/courses")
async def read_courses():
    return {"courses": []}