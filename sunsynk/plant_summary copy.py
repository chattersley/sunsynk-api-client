from dataclasses import dataclass
from marshmallow import Schema, fields, post_load


@dataclass
class PlantSummary:
    id: int
    name: str
    type: int
    master: str | None
    installer: str | None
    email: str | None
    phone: str | None


class PlantSummarySchema(Schema):
    @post_load
    def make_plant_summary(self, data, **kwargs):
        return PlantSummary(**data)

    id = fields.Integer(required=True)
    name = fields.Str(required=True)
    type = fields.Integer(required=True)
    master = fields.Str(allow_none=True)
    installer = fields.Str(allow_none=True)
    email = fields.Str(allow_none=True)
    phone = fields.Str(allow_none=True)
