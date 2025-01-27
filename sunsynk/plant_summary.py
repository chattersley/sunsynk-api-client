from sunsynk.resource import Resource


class PlantSummary(Resource):
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.type = data.get("type")
        self.master = data.get("master")
        self.installer = data.get("installer")
        self.email = data.get("email")
        self.phone = data.get("phone")
