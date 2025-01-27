from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from datetime import datetime
from marshmallow import fields
from typing import Optional


@dataclass_json
@dataclass
class Notification:
    id: int
    type: int
    status: int
    message_type: int = field(metadata=config(field_name="messageType"))
    user_id: int = field(metadata=config(field_name="userId"))
    created_at: datetime = field(
        metadata=config(
            field_name="createAt",
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format="iso"),
        )
    )
    station_name: Optional[str] = field(metadata=config(field_name="stationName"))
    start_time: Optional[datetime] = field(
        metadata=config(
            field_name="startTime",
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format="iso"),
        )
    )
    end_time: Optional[datetime] = field(
        metadata=config(
            field_name="endTime",
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format="iso"),
        )
    )
    description: str
    sn: Optional[str]
    soc: Optional[str]
