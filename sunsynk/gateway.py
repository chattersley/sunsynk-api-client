from sunsynk.plant_summary import PlantSummary

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from datetime import datetime
from marshmallow import fields, Schema
# from marshmallow.fields import String


@dataclass_json
@dataclass
class Gateway:
    id: int
    sn: str
    key: str
    status: int
    communication_type: int = field(metadata=config(field_name="commType"))
    signal: int
    # software_version: str = fields.Str(data_key="softVer")
    software_version: str = field(metadata=config(field_name="softVer"))
    hardware_version: str = field(metadata=config(field_name="hardVer"))
    updated_at: str = field(metadata=config(field_name="updateAt"))
    # updated_at: datetime = field(
    #     metadata=config(
    #         field_name="updateAt",
    #         encoder=datetime.isoformat,
    #         decoder=datetime.fromisoformat,
    #         mm_field=fields.DateTime(format="iso"),
    #     )
    # )
    protocol_type: int = field(metadata=config(field_name="protocolType"))
    model: str
    alias: str | None
    lldt: datetime = field(
        metadata=config(
            field_name="lldt",
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format="iso"),
        )
    )
    upload_cycle: int = field(metadata=config(field_name="uploadCycle"))
    sgcc: int
    iccid: str
    device_name: str = field(metadata=config(field_name="devName"))
    server_id: str | None = field(metadata=config(field_name="serverId"))
    server_name: str | None = field(metadata=config(field_name="serverName"))
    brand: str | None
    plant: PlantSummary
    agent: str | None
    communication_type_name: str = field(metadata=config(field_name="commTypeName"))
    proto: str
    do_sum: str | None = field(metadata=config(field_name="doSum"))
    do_state: str | None = field(metadata=config(field_name="doState"))
