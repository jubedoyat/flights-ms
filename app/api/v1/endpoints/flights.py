from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from app.models.flight import FlightBase, FlightPublic
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

@router.get("/{flight_id}", response_model=FlightPublic)
async def get_flight_by_id(
    flight_id: str = Path(..., description="MongoDB ObjectID of the flight"),
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    if not ObjectId.is_valid(flight_id):
        raise HTTPException(status_code=400, detail="Invalid flight ID")

    flight = await db["Flights"].find_one({"_id": ObjectId(flight_id)})

    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")

    flight["_id"] = str(flight["_id"])
    return FlightPublic(**flight)

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