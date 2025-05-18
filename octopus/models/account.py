from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Register(BaseModel):
    identifier: str
    rate: str
    is_settlement_register: bool


class Meter(BaseModel):
    serial_number: str
    registers: Optional[list[Register]] = None


class Agreement(BaseModel):
    tariff_code: str
    valid_from: datetime
    valid_to: Optional[datetime] = None


class MeterPoint(BaseModel):
    consumption_standard: int
    meters: list[Meter]
    agreements: list[Agreement]


class ElectricityMeterPoint(MeterPoint):
    mpan: str
    profile_class: int
    is_export: bool


class GasMeterPoint(MeterPoint):
    mprn: str


class AccountProperties(BaseModel):
    id: int
    moved_in_at: datetime
    moved_out_at: Optional[datetime] = None
    address_line_1: str
    address_line_2: str
    address_line_3: str
    town: str
    county: str
    postcode: str
    electricity_meter_points: list[ElectricityMeterPoint]
    gas_meter_points: list[GasMeterPoint]


class Account(BaseModel):
    number: str
    properties: list[AccountProperties]
