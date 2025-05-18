from pydantic import BaseModel, ConfigDict, alias_generators 
from typing import Literal, Optional

class Product(BaseModel):
    model_config = ConfigDict(alias_generator=alias_generators.to_camel)

    direction: int
    rates_threshold: int
    provider: int
    limit_soc: Optional[int]
    region_id: int

class ChargePrice(BaseModel):
    model_config = ConfigDict(alias_generator=alias_generators.to_camel)

    type: str
    price: str
    start_range: str
    end_range: str

class ConstantPrice(ChargePrice):
    type: Literal["1"]
    start_range: str = "00:00"
    end_range: str = "24:00"

class TimeOfUsePrice(ChargePrice):
    type: Literal["2"]

class LivePrice(ChargePrice):
    type: Literal["3"]
    start_range: str = ""
    end_range: str = ""
    price: str  = "0"

class PlantIncome(BaseModel):
    model_config = ConfigDict(exclude_none=True)

    id: str
    currency: int
    invest: float
    charges: list[ConstantPrice] | list[TimeOfUsePrice] | list[LivePrice]
    products: Optional[list[Product]] = None
