from sunsynk.plant_income import PlantIncome
from pydantic_core import from_json, ValidationError
import pytest

constant_price= """{
  "id": "123456",
  "currency": 366,
  "invest": 5002.12,
  "charges": [
    { "price": "100", "type": "1", "startRange": "00:00", "endRange": "24:00" }
  ]
}"""

invalid_constant_price= """{
  "id": "123456",
  "invest": 5002.12,
  "charges": [
    { "price": 1.2, "type": "1", "endRange": "22:00" }
  ]
}"""

time_of_use_price= """{
  "id": "234567",
  "currency": 366,
  "invest": 1030.19,
  "charges": [
    { "startRange": "00:00", "endRange": "10:15", "price": "10", "type": "2" },
    { "startRange": "10:15", "endRange": "23:00", "price": "40", "type": "2" },
    { "startRange": "23:00", "endRange": "24:00", "price": "33", "type": "2" }
  ]
}"""

live_price= """{
  "id": "456789",
  "currency": 366,
  "invest": 1730.11,
  "charges": [{ "price": "0", "type": "3", "startRange": "", "endRange": "" }],
  "products": [
    {
      "direction": 1,
      "ratesThreshold": 20,
      "provider": 1,
      "limitSoc": null,
      "regionId": 8
    },
    {
      "direction": 0,
      "ratesThreshold": 23,
      "provider": 1,
      "limitSoc": 20,
      "regionId": 8
    }
  ]
}"""

def test_parse_constant_price():
    income = PlantIncome.model_validate(from_json(constant_price))

    assert income.id == "123456"
    assert income.currency == 366
    assert income.invest == pytest.approx(5002.12, abs=0.0)
    assert income.charges[0].price == "100"
    assert income.charges[0].type == "1"
    assert income.charges[0].start_range == "00:00"
    assert income.charges[0].end_range ==  "24:00"
    
def test_parse_invalid_constant_price():

    with pytest.raises(ValidationError) as excinfo:  
      PlantIncome.model_validate(from_json(invalid_constant_price))

    assert str(excinfo.value) == """7 validation errors for PlantIncome
currency
  Field required [type=missing, input_value={'id': '123456', 'invest'..., 'endRange': '22:00'}]}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing
charges.list[ConstantPrice].0.price
  Input should be a valid string [type=string_type, input_value=1.2, input_type=float]
    For further information visit https://errors.pydantic.dev/2.10/v/string_type
charges.list[TimeOfUsePrice].0.type
  Input should be '2' [type=literal_error, input_value='1', input_type=str]
    For further information visit https://errors.pydantic.dev/2.10/v/literal_error
charges.list[TimeOfUsePrice].0.price
  Input should be a valid string [type=string_type, input_value=1.2, input_type=float]
    For further information visit https://errors.pydantic.dev/2.10/v/string_type
charges.list[TimeOfUsePrice].0.startRange
  Field required [type=missing, input_value={'price': 1.2, 'type': '1', 'endRange': '22:00'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing
charges.list[LivePrice].0.type
  Input should be '3' [type=literal_error, input_value='1', input_type=str]
    For further information visit https://errors.pydantic.dev/2.10/v/literal_error
charges.list[LivePrice].0.price
  Input should be a valid string [type=string_type, input_value=1.2, input_type=float]
    For further information visit https://errors.pydantic.dev/2.10/v/string_type"""

def test_parse_time_of_use_price():
    income = PlantIncome.model_validate(from_json(time_of_use_price))

    assert income.id == "234567"
    assert income.currency == 366
    assert income.invest == pytest.approx(1030.19, abs=0.0)
    assert income.charges[0].price == "10"
    assert income.charges[0].type == "2"
    assert income.charges[0].start_range == "00:00"
    assert income.charges[0].end_range ==  "10:15"
    assert income.charges[1].price == "40"
    assert income.charges[1].type == "2"
    assert income.charges[1].start_range == "10:15"
    assert income.charges[1].end_range ==  "23:00"
    assert income.charges[2].price == "33"
    assert income.charges[2].type == "2"
    assert income.charges[2].start_range == "23:00"
    assert income.charges[2].end_range ==  "24:00"


def test_parse_live_price():
    income = PlantIncome.model_validate(from_json(live_price))

    assert income.id == "456789"
    assert income.currency == 366
    assert income.invest == pytest.approx(1730.11, abs=0.0)
    assert income.charges[0].price == "0"
    assert income.charges[0].type == "3"
    assert income.charges[0].start_range == ""
    assert income.charges[0].end_range ==  ""

    assert income.products[0].direction ==  1
    assert income.products[0].rates_threshold ==  20
    assert income.products[0].provider ==  1
    assert income.products[0].limit_soc ==  None
    assert income.products[0].region_id ==  8

    assert income.products[1].direction ==  0
    assert income.products[1].rates_threshold ==  23
    assert income.products[1].provider ==  1
    assert income.products[1].limit_soc ==  20
    assert income.products[1].region_id ==  8


# def test_parse_invalid_plant():

#     with pytest.raises(ValidationError) as excinfo:  
#       PlantSummary.model_validate(from_json(invalid_plant_summary))

#     assert str(excinfo.value) == """2 validation errors for PlantSummary
# id
#   Input should be a valid integer [type=int_type, input_value=None, input_type=NoneType]
#     For further information visit https://errors.pydantic.dev/2.10/v/int_type
# name
#   Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
#     For further information visit https://errors.pydantic.dev/2.10/v/string_type"""
