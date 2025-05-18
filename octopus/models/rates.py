from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class HistoricalCharge(BaseModel):
    payment_method: Optional[str] = None
    valid_from: Optional[datetime] = None
    valid_to: Optional[datetime] = None
    value_exc_vat: float
    value_inc_vat: float


class Rates(BaseModel):
    count: int
    results: list[HistoricalCharge]
    next: Optional[str] = None
    previous: Optional[str] = None
