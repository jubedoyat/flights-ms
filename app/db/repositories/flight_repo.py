from typing import List, Optional
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models.flight import FlightInDB

class FlightRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db["Flights"]

    async def get_all_flights(self):
        flights = []
        async for doc in self.collection.find():
            doc["flight_id"] = str(doc["flight_id"])
            flights.append(FlightInDB(**doc))
        return flights

    async def find_by_filters(
        self,
        date: Optional[str] = None,
        origin: Optional[str] = None,
        destiny: Optional[str] = None
    ) -> List[FlightInDB]:
        query = {}

        if date:
            query["departure.date"] = date
        if origin:
            query["departure.origin"] = origin
        if destiny:
            query["arriving.destiny"] = destiny

        flights = []
        async for doc in self.collection.find(query):
            doc["flight_id"] = str(doc["flight_id"])
            flights.append(FlightInDB(**doc))

        return flights