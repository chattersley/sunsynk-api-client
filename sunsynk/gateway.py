import datetime

from sunsynk.resource import Resource
from sunsynk.plant_summary import PlantSummary


class Gateway(Resource):
    def __init__(self, data):
        self.id = data["id"]
        self.sn = data["sn"]
        self.key = data["key"]
        self.status = data["status"]
        self.communication_type = data["commType"]
        self.signal = data["signal"]
        self.software_version = data["softVer"]
        self.hardware_version = data["hardVer"]
        self.updated_at = datetime.datetime.strptime(
            data["updateAt"], "%Y-%m-%dT%H:%M:%SZ"
        )
        self.protocolType = data["protocolType"]
        self.model = data["model"]
        self.alias = data["alias"]
        self.lldt = datetime.datetime.strptime(data["lldt"], "%Y-%m-%dT%H:%M:%SZ")
        self.upload_cycle = data["uploadCycle"]
        self.sgcc = data["sgcc"]
        self.iccid = data["iccid"]
        self.device_name = data["devName"]
        self.server_id = data["serverId"]
        self.server_name = data["serverName"]
        self.brand = data["brand"]
        self.plant = PlantSummary(data.get("plant")) if "plant" in data.keys() else None
        self.agent = data["agent"]
        self.communication_type_name = data["commTypeName"]
        self.proto = data["proto"]
        self.do_sum = data["doSum"]
        self.do_state = data["doState"]
