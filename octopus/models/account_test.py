from octopus.models.account import Account
from pydantic_core import from_json, ValidationError
from sunsynk.octopus import extract_product_code
import pytest
import pandas as pd
import logging

account_response = """{
  "number": "A-C5F08372",
  "properties": [
    {
      "id": 5024296,
      "moved_in_at": "2021-10-21T00:00:00+01:00",
      "moved_out_at": null,
      "address_line_1": "88",
      "address_line_2": "OLD STREET ROAD",
      "address_line_3": "WINCHESTER",
      "town": "HAMPSHIRE",
      "county": "",
      "postcode": "SO23 0LB",
      "electricity_meter_points": [
        {
          "mpan": "2000017082844",
          "profile_class": 1,
          "consumption_standard": 9687,
          "meters": [
            {
              "serial_number": "F02C54625",
              "registers": [
                {
                  "identifier": "01",
                  "rate": "STANDARD",
                  "is_settlement_register": true
                }
              ]
            },
            {
              "serial_number": "22J0277224",
              "registers": [
                {
                  "identifier": "1",
                  "rate": "STANDARD",
                  "is_settlement_register": true
                }
              ]
            }
          ],
          "agreements": [
            {
              "tariff_code": "E-1R-BULB-CRED-VAR-V1-H",
              "valid_from": "2021-10-23T00:00:00+01:00",
              "valid_to": "2023-04-01T00:00:00+01:00"
            },
            {
              "tariff_code": "E-1R-VAR-BB-23-04-01-H",
              "valid_from": "2023-04-01T00:00:00+01:00",
              "valid_to": "2023-09-05T00:00:00+01:00"
            },
            {
              "tariff_code": "E-1R-AGILE-FLEX-BB-23-02-08-H",
              "valid_from": "2023-09-05T00:00:00+01:00",
              "valid_to": "2024-02-15T00:00:00Z"
            },
            {
              "tariff_code": "E-1R-AGILE-BB-23-12-06-H",
              "valid_from": "2024-02-15T00:00:00Z",
              "valid_to": "2025-02-15T00:00:00Z"
            },
            {
              "tariff_code": "E-1R-VAR-BB-23-04-01-H",
              "valid_from": "2025-02-15T00:00:00Z",
              "valid_to": "2025-02-15T00:00:00Z"
            },
            {
              "tariff_code": "E-1R-AGILE-BB-24-10-01-H",
              "valid_from": "2025-02-15T00:00:00Z",
              "valid_to": "2026-02-15T00:00:00Z"
            }
          ],
          "is_export": false
        }
      ],
      "gas_meter_points": [
        {
          "mprn": "3969477010",
          "consumption_standard": 24661,
          "meters": [
            {
              "serial_number": "E6S18664862261"
            },
            {
              "serial_number": "3057022"
            }
          ],
          "agreements": [
            {
              "tariff_code": "G-1R-BULB-CRED-VAR-V1-H",
              "valid_from": "2021-10-23T00:00:00+01:00",
              "valid_to": "2023-04-01T00:00:00+01:00"
            },
            {
              "tariff_code": "G-1R-VAR-BB-23-04-01-H",
              "valid_from": "2023-04-01T00:00:00+01:00",
              "valid_to": null
            }
          ]
        }
      ]
    }
  ]
}"""


def test_parse_account():
    account = Account.model_validate(from_json(account_response))

    assert account.number == "A-C5F08372"

    agreements = pd.DataFrame.from_records(
        account.properties[0].electricity_meter_points[0].agreements,
        columns=["tariff_code", "valid_from", "valid_to"],
    )

    logging.debug(
        f"Account valid to: {agreements.iloc[agreements['valid_to'].argmax()]}"
    )
    logging.debug(
        f"Account valid to: {(agreements.iloc[agreements['valid_to'].argmax()].loc['tariff_code'][1])}"
    )
    logging.debug(
        f"Account valid to: {(agreements.iloc[agreements['valid_to'].argmax()].loc['tariff_code'])}"
    )

    logging.debug(extract_product_code(agreements.iloc[agreements['valid_to'].argmax()].loc['tariff_code'][1]))