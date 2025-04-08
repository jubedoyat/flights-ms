from pydantic import BaseModel, Field
from datetime import datetime

class FlightDeparture(BaseModel):
    date: datetime
    airport: str

class FlightArriving(BaseModel):
    date: datetime
    airport: str

class FlightBase(BaseModel):
    flight_id: str
    departure: FlightDeparture
    arriving: FlightArriving
    airline: str
    airplane: str

class FlightInDB(FlightBase):
    id: str = Field(..., alias="flight_id")

    class Config:
        from_attributes = True
        validate_by_name = True