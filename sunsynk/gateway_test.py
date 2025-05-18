from sunsynk.gateway import Gateway

minimal_gateway = """{
        "id": 1234567,
        "sn": "E4701559Q577",
        "key": "DLQTLNAS",
        "status": 2,
        "commType": 2,
        "signal": -82,
        "softVer": "4790123B24R",
        "hardVer": "AEW2-0005-03",
        "updateAt": "2025-01-31T19:57:32Z",
        "protocolType": 29,
        "model": "EESW-D205",
        "alias": null,
        "lldt": "2025-01-31T19:57:32Z",
        "uploadCycle": 300,
        "sgcc": 1,
        "iccid": "",
        "devName": "magpie",
        "serverId": null,
        "serverName": null,
        "brand": null,
        "plant": {
          "id": 345964,
          "name": "Smith",
          "type": 2,
          "master": "admin@solarfarm.co.uk",
          "installer": null,
          "email": null,
          "phone": null
        },
        "agent": null,
        "commTypeName": "Wi-Fi",
        "proto": "Deye",
        "doSum": null,
        "doState": null
      }"""


def test_parse_minimal_gateway():
    y = Gateway.schema().loads(minimal_gateway)  # , many=True
