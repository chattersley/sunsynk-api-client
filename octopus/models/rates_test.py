import logging
from urllib.parse import urlencode
from octopus.models.rates import Rates
from pydantic_core import from_json, ValidationError


def clean_nones(value):
    """
    Recursively remove all None values from dictionaries and lists, and returns
    the result as a new dictionary or list.
    """
    if isinstance(value, list):
        return [clean_nones(x) for x in value if x is not None]
    elif isinstance(value, dict):
        return {
            key: clean_nones(val)
            for key, val in value.items()
            if val is not None
        }
    else:
        return value

def test_why():
    params = urlencode(clean_nones({"period_from": "ssss", "period_to": None}))
    logging.debug(f"params: {params}")
    params = urlencode(clean_nones({"period_from": None, "period_to": None}))
    logging.debug(f"params: {f'?{params}' if len(params) > 0 else ''}")

rates_response = """{
  "count": 11518,
  "next": "https://api.octopus.energy/v1/products/AGILE-24-10-01/electricity-tariffs/E-1R-AGILE-24-10-01-H/standard-unit-rates/?page=2",
  "previous": null,
  "results": [
    {
      "value_exc_vat": 16.46,
      "value_inc_vat": 17.283,
      "valid_from": "2025-05-13T21:30:00Z",
      "valid_to": "2025-05-13T22:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 19.28,
      "value_inc_vat": 20.244,
      "valid_from": "2025-05-13T21:00:00Z",
      "valid_to": "2025-05-13T21:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 20.5,
      "value_inc_vat": 21.525,
      "valid_from": "2025-05-13T20:30:00Z",
      "valid_to": "2025-05-13T21:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 20.59,
      "value_inc_vat": 21.6195,
      "valid_from": "2025-05-13T20:00:00Z",
      "valid_to": "2025-05-13T20:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 22.36,
      "value_inc_vat": 23.478,
      "valid_from": "2025-05-13T19:30:00Z",
      "valid_to": "2025-05-13T20:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 22.26,
      "value_inc_vat": 23.373,
      "valid_from": "2025-05-13T19:00:00Z",
      "valid_to": "2025-05-13T19:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 22.51,
      "value_inc_vat": 23.6355,
      "valid_from": "2025-05-13T18:30:00Z",
      "valid_to": "2025-05-13T19:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 22.42,
      "value_inc_vat": 23.541,
      "valid_from": "2025-05-13T18:00:00Z",
      "valid_to": "2025-05-13T18:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 31.66,
      "value_inc_vat": 33.243,
      "valid_from": "2025-05-13T17:30:00Z",
      "valid_to": "2025-05-13T18:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 31.4,
      "value_inc_vat": 32.97,
      "valid_from": "2025-05-13T17:00:00Z",
      "valid_to": "2025-05-13T17:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 28.39,
      "value_inc_vat": 29.8095,
      "valid_from": "2025-05-13T16:30:00Z",
      "valid_to": "2025-05-13T17:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 26.18,
      "value_inc_vat": 27.489,
      "valid_from": "2025-05-13T16:00:00Z",
      "valid_to": "2025-05-13T16:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 26.15,
      "value_inc_vat": 27.4575,
      "valid_from": "2025-05-13T15:30:00Z",
      "valid_to": "2025-05-13T16:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 26.18,
      "value_inc_vat": 27.489,
      "valid_from": "2025-05-13T15:00:00Z",
      "valid_to": "2025-05-13T15:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.7,
      "value_inc_vat": 15.435,
      "valid_from": "2025-05-13T14:30:00Z",
      "valid_to": "2025-05-13T15:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.18,
      "value_inc_vat": 14.889,
      "valid_from": "2025-05-13T14:00:00Z",
      "valid_to": "2025-05-13T14:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.18,
      "value_inc_vat": 14.889,
      "valid_from": "2025-05-13T13:30:00Z",
      "valid_to": "2025-05-13T14:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.3,
      "value_inc_vat": 15.015,
      "valid_from": "2025-05-13T13:00:00Z",
      "valid_to": "2025-05-13T13:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.18,
      "value_inc_vat": 14.889,
      "valid_from": "2025-05-13T12:30:00Z",
      "valid_to": "2025-05-13T13:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.28,
      "value_inc_vat": 14.994,
      "valid_from": "2025-05-13T12:00:00Z",
      "valid_to": "2025-05-13T12:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.28,
      "value_inc_vat": 14.994,
      "valid_from": "2025-05-13T11:30:00Z",
      "valid_to": "2025-05-13T12:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.28,
      "value_inc_vat": 14.994,
      "valid_from": "2025-05-13T11:00:00Z",
      "valid_to": "2025-05-13T11:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.28,
      "value_inc_vat": 14.994,
      "valid_from": "2025-05-13T10:30:00Z",
      "valid_to": "2025-05-13T11:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 15.37,
      "value_inc_vat": 16.1385,
      "valid_from": "2025-05-13T10:00:00Z",
      "valid_to": "2025-05-13T10:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 15.56,
      "value_inc_vat": 16.338,
      "valid_from": "2025-05-13T09:30:00Z",
      "valid_to": "2025-05-13T10:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 17.06,
      "value_inc_vat": 17.913,
      "valid_from": "2025-05-13T09:00:00Z",
      "valid_to": "2025-05-13T09:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 18.7,
      "value_inc_vat": 19.635,
      "valid_from": "2025-05-13T08:30:00Z",
      "valid_to": "2025-05-13T09:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 19.74,
      "value_inc_vat": 20.727,
      "valid_from": "2025-05-13T08:00:00Z",
      "valid_to": "2025-05-13T08:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 19.73,
      "value_inc_vat": 20.7165,
      "valid_from": "2025-05-13T07:30:00Z",
      "valid_to": "2025-05-13T08:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 22.26,
      "value_inc_vat": 23.373,
      "valid_from": "2025-05-13T07:00:00Z",
      "valid_to": "2025-05-13T07:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 23.52,
      "value_inc_vat": 24.696,
      "valid_from": "2025-05-13T06:30:00Z",
      "valid_to": "2025-05-13T07:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 20.96,
      "value_inc_vat": 22.008,
      "valid_from": "2025-05-13T06:00:00Z",
      "valid_to": "2025-05-13T06:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 22.65,
      "value_inc_vat": 23.7825,
      "valid_from": "2025-05-13T05:30:00Z",
      "valid_to": "2025-05-13T06:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 20.37,
      "value_inc_vat": 21.3885,
      "valid_from": "2025-05-13T05:00:00Z",
      "valid_to": "2025-05-13T05:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 16.38,
      "value_inc_vat": 17.199,
      "valid_from": "2025-05-13T04:30:00Z",
      "valid_to": "2025-05-13T05:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 17.18,
      "value_inc_vat": 18.039,
      "valid_from": "2025-05-13T04:00:00Z",
      "valid_to": "2025-05-13T04:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 15.33,
      "value_inc_vat": 16.0965,
      "valid_from": "2025-05-13T03:30:00Z",
      "valid_to": "2025-05-13T04:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 15.37,
      "value_inc_vat": 16.1385,
      "valid_from": "2025-05-13T03:00:00Z",
      "valid_to": "2025-05-13T03:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.28,
      "value_inc_vat": 14.994,
      "valid_from": "2025-05-13T02:30:00Z",
      "valid_to": "2025-05-13T03:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.56,
      "value_inc_vat": 15.288,
      "valid_from": "2025-05-13T02:00:00Z",
      "valid_to": "2025-05-13T02:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.25,
      "value_inc_vat": 14.9625,
      "valid_from": "2025-05-13T01:30:00Z",
      "valid_to": "2025-05-13T02:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.6,
      "value_inc_vat": 15.33,
      "valid_from": "2025-05-13T01:00:00Z",
      "valid_to": "2025-05-13T01:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.13,
      "value_inc_vat": 14.8365,
      "valid_from": "2025-05-13T00:30:00Z",
      "valid_to": "2025-05-13T01:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 13.86,
      "value_inc_vat": 14.553,
      "valid_from": "2025-05-13T00:00:00Z",
      "valid_to": "2025-05-13T00:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.12,
      "value_inc_vat": 14.826,
      "valid_from": "2025-05-12T23:30:00Z",
      "valid_to": "2025-05-13T00:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.45,
      "value_inc_vat": 15.1725,
      "valid_from": "2025-05-12T23:00:00Z",
      "valid_to": "2025-05-12T23:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 15.37,
      "value_inc_vat": 16.1385,
      "valid_from": "2025-05-12T22:30:00Z",
      "valid_to": "2025-05-12T23:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 16.09,
      "value_inc_vat": 16.8945,
      "valid_from": "2025-05-12T22:00:00Z",
      "valid_to": "2025-05-12T22:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.78,
      "value_inc_vat": 15.519,
      "valid_from": "2025-05-12T21:30:00Z",
      "valid_to": "2025-05-12T22:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 16.17,
      "value_inc_vat": 16.9785,
      "valid_from": "2025-05-12T21:00:00Z",
      "valid_to": "2025-05-12T21:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 17.32,
      "value_inc_vat": 18.186,
      "valid_from": "2025-05-12T20:30:00Z",
      "valid_to": "2025-05-12T21:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 19.25,
      "value_inc_vat": 20.2125,
      "valid_from": "2025-05-12T20:00:00Z",
      "valid_to": "2025-05-12T20:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 21.0,
      "value_inc_vat": 22.05,
      "valid_from": "2025-05-12T19:30:00Z",
      "valid_to": "2025-05-12T20:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 20.9,
      "value_inc_vat": 21.945,
      "valid_from": "2025-05-12T19:00:00Z",
      "valid_to": "2025-05-12T19:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 21.84,
      "value_inc_vat": 22.932,
      "valid_from": "2025-05-12T18:30:00Z",
      "valid_to": "2025-05-12T19:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 20.66,
      "value_inc_vat": 21.693,
      "valid_from": "2025-05-12T18:00:00Z",
      "valid_to": "2025-05-12T18:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 32.73,
      "value_inc_vat": 34.3665,
      "valid_from": "2025-05-12T17:30:00Z",
      "valid_to": "2025-05-12T18:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 32.43,
      "value_inc_vat": 34.0515,
      "valid_from": "2025-05-12T17:00:00Z",
      "valid_to": "2025-05-12T17:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 29.64,
      "value_inc_vat": 31.122,
      "valid_from": "2025-05-12T16:30:00Z",
      "valid_to": "2025-05-12T17:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 28.63,
      "value_inc_vat": 30.0615,
      "valid_from": "2025-05-12T16:00:00Z",
      "valid_to": "2025-05-12T16:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 27.54,
      "value_inc_vat": 28.917,
      "valid_from": "2025-05-12T15:30:00Z",
      "valid_to": "2025-05-12T16:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 27.16,
      "value_inc_vat": 28.518,
      "valid_from": "2025-05-12T15:00:00Z",
      "valid_to": "2025-05-12T15:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.7,
      "value_inc_vat": 15.435,
      "valid_from": "2025-05-12T14:30:00Z",
      "valid_to": "2025-05-12T15:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 13.86,
      "value_inc_vat": 14.553,
      "valid_from": "2025-05-12T14:00:00Z",
      "valid_to": "2025-05-12T14:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.64,
      "value_inc_vat": 15.372,
      "valid_from": "2025-05-12T13:30:00Z",
      "valid_to": "2025-05-12T14:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.64,
      "value_inc_vat": 15.372,
      "valid_from": "2025-05-12T13:00:00Z",
      "valid_to": "2025-05-12T13:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.23,
      "value_inc_vat": 14.9415,
      "valid_from": "2025-05-12T12:30:00Z",
      "valid_to": "2025-05-12T13:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.24,
      "value_inc_vat": 14.952,
      "valid_from": "2025-05-12T12:00:00Z",
      "valid_to": "2025-05-12T12:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 15.79,
      "value_inc_vat": 16.5795,
      "valid_from": "2025-05-12T11:30:00Z",
      "valid_to": "2025-05-12T12:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 15.77,
      "value_inc_vat": 16.5585,
      "valid_from": "2025-05-12T11:00:00Z",
      "valid_to": "2025-05-12T11:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 17.01,
      "value_inc_vat": 17.8605,
      "valid_from": "2025-05-12T10:30:00Z",
      "valid_to": "2025-05-12T11:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 18.07,
      "value_inc_vat": 18.9735,
      "valid_from": "2025-05-12T10:00:00Z",
      "valid_to": "2025-05-12T10:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 18.34,
      "value_inc_vat": 19.257,
      "valid_from": "2025-05-12T09:30:00Z",
      "valid_to": "2025-05-12T10:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 17.91,
      "value_inc_vat": 18.8055,
      "valid_from": "2025-05-12T09:00:00Z",
      "valid_to": "2025-05-12T09:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 18.48,
      "value_inc_vat": 19.404,
      "valid_from": "2025-05-12T08:30:00Z",
      "valid_to": "2025-05-12T09:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 19.82,
      "value_inc_vat": 20.811,
      "valid_from": "2025-05-12T08:00:00Z",
      "valid_to": "2025-05-12T08:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 18.96,
      "value_inc_vat": 19.908,
      "valid_from": "2025-05-12T07:30:00Z",
      "valid_to": "2025-05-12T08:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 19.74,
      "value_inc_vat": 20.727,
      "valid_from": "2025-05-12T07:00:00Z",
      "valid_to": "2025-05-12T07:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 20.5,
      "value_inc_vat": 21.525,
      "valid_from": "2025-05-12T06:30:00Z",
      "valid_to": "2025-05-12T07:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 18.9,
      "value_inc_vat": 19.845,
      "valid_from": "2025-05-12T06:00:00Z",
      "valid_to": "2025-05-12T06:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 18.31,
      "value_inc_vat": 19.2255,
      "valid_from": "2025-05-12T05:30:00Z",
      "valid_to": "2025-05-12T06:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 15.75,
      "value_inc_vat": 16.5375,
      "valid_from": "2025-05-12T05:00:00Z",
      "valid_to": "2025-05-12T05:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 15.75,
      "value_inc_vat": 16.5375,
      "valid_from": "2025-05-12T04:30:00Z",
      "valid_to": "2025-05-12T05:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 16.01,
      "value_inc_vat": 16.8105,
      "valid_from": "2025-05-12T04:00:00Z",
      "valid_to": "2025-05-12T04:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.28,
      "value_inc_vat": 14.994,
      "valid_from": "2025-05-12T03:30:00Z",
      "valid_to": "2025-05-12T04:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 15.08,
      "value_inc_vat": 15.834,
      "valid_from": "2025-05-12T03:00:00Z",
      "valid_to": "2025-05-12T03:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 13.44,
      "value_inc_vat": 14.112,
      "valid_from": "2025-05-12T02:30:00Z",
      "valid_to": "2025-05-12T03:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 13.94,
      "value_inc_vat": 14.637,
      "valid_from": "2025-05-12T02:00:00Z",
      "valid_to": "2025-05-12T02:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 13.65,
      "value_inc_vat": 14.3325,
      "valid_from": "2025-05-12T01:30:00Z",
      "valid_to": "2025-05-12T02:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 14.28,
      "value_inc_vat": 14.994,
      "valid_from": "2025-05-12T01:00:00Z",
      "valid_to": "2025-05-12T01:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 13.69,
      "value_inc_vat": 14.3745,
      "valid_from": "2025-05-12T00:30:00Z",
      "valid_to": "2025-05-12T01:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 13.69,
      "value_inc_vat": 14.3745,
      "valid_from": "2025-05-12T00:00:00Z",
      "valid_to": "2025-05-12T00:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 13.65,
      "value_inc_vat": 14.3325,
      "valid_from": "2025-05-11T23:30:00Z",
      "valid_to": "2025-05-12T00:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 13.84,
      "value_inc_vat": 14.532,
      "valid_from": "2025-05-11T23:00:00Z",
      "valid_to": "2025-05-11T23:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 13.44,
      "value_inc_vat": 14.112,
      "valid_from": "2025-05-11T22:30:00Z",
      "valid_to": "2025-05-11T23:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 13.87,
      "value_inc_vat": 14.5635,
      "valid_from": "2025-05-11T22:00:00Z",
      "valid_to": "2025-05-11T22:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 13.84,
      "value_inc_vat": 14.532,
      "valid_from": "2025-05-11T21:30:00Z",
      "valid_to": "2025-05-11T22:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 15.15,
      "value_inc_vat": 15.9075,
      "valid_from": "2025-05-11T21:00:00Z",
      "valid_to": "2025-05-11T21:30:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 16.26,
      "value_inc_vat": 17.073,
      "valid_from": "2025-05-11T20:30:00Z",
      "valid_to": "2025-05-11T21:00:00Z",
      "payment_method": null
    },
    {
      "value_exc_vat": 17.9,
      "value_inc_vat": 18.795,
      "valid_from": "2025-05-11T20:00:00Z",
      "valid_to": "2025-05-11T20:30:00Z",
      "payment_method": null
    }
  ]
}"""



def test_parse_rates():
    rates = Rates.model_validate(from_json(rates_response))

    assert rates.count == 11518