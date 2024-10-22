from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from src.agents.sport_drills_agent import SportAgent



router = APIRouter()



class SportInfo(BaseModel):
    sport_name: str
    sport_skill_level: str



@router.get("/test-sport")  # Add a test GET route
def test_sport():
    return {"message": "Sport route is working"}

@router.post("/sportinfo/")  # Note: removed trailing slash
async def get_sport_info(sport_info: SportInfo):
    """Get sports drills"""
    try:
        response = await SportAgent.generate_sports_drills(
            sport_info.sport_name, 
            sport_info.sport_skill_level
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))