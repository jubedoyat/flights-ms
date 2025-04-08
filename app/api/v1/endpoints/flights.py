from fastapi import APIRouter, Depends, Query
from app.models.flight import FlightBase
from app.db.repositories.flight_repo import FlightRepository
from app.db.mongodb import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import List, Optional

router = APIRouter(prefix="/flights", tags=["Flights"])

@router.get("/", response_model=List[FlightBase])
async def get_all_flights(db: AsyncIOMotorDatabase = Depends(get_database)):
    repo = FlightRepository(db)
    flights = await repo.get_all_flights()
    return flights

@router.get("/search", response_model=List[FlightBase])
async def search_flights(
    date: Optional[str] = Query(None, example="2025-04-10"),
    origin: Optional[str] = Query(None, example="Bogotá"),
    destiny: Optional[str] = Query(None, example="New York"),
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    repo = FlightRepository(db)
    results = await repo.find_by_filters(date=date, origin=origin, destiny=destiny)
    return results