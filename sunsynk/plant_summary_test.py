from sunsynk.plant_summary import PlantSummary
from pydantic_core import from_json, ValidationError
import pytest

minimal_plant_summary = """{
          "id": 123456,
          "name": "Smith",
          "type": 2,
          "master": null,
          "installer": null,
          "email": null,
          "phone": null
        }"""

complete_plant_summary = """{
          "id": 123456,
          "name": "Smith",
          "type": 2,
          "master": "my@installer.com",
          "installer": "Bob the Installer",
          "email": "anemail@address.com",
          "phone": "079898944"
        }"""

invalid_plant_summary = """{
          "id": null,
          "name": null,
          "type": 2,
          "master": null,
          "installer": null,
          "email": null,
          "phone": null
        }"""


def test_parse_minimal_plant():
    y = PlantSummary.model_validate(from_json(minimal_plant_summary))

    assert y.id == 123456
    assert y.name == "Smith"
    assert y.type == 2
    assert y.master == None


def test_parse_full_plant():
    y = PlantSummary.model_validate(from_json(complete_plant_summary))

    assert y.id == 123456
    assert y.name == "Smith"
    assert y.type == 2
    assert y.master == "my@installer.com"
    assert y.installer == "Bob the Installer"
    assert y.email == "anemail@address.com"
    assert y.phone == "079898944"


def test_parse_invalid_plant():

    with pytest.raises(ValidationError) as excinfo:  
      PlantSummary.model_validate(from_json(invalid_plant_summary))

    assert str(excinfo.value) == """2 validation errors for PlantSummary
id
  Input should be a valid integer [type=int_type, input_value=None, input_type=NoneType]
    For further information visit https://errors.pydantic.dev/2.10/v/int_type
name
  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
    For further information visit https://errors.pydantic.dev/2.10/v/string_type"""
