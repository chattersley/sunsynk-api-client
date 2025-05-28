import aiohttp
from aiohttp import BasicAuth
from datetime import datetime
from typing import Optional
from urllib.parse import urlencode
import logging
from octopus.utils import clean_nones

from octopus.models.account import Account
from octopus.models.rates import Rates


class InvalidCredentialsException(Exception):
    def __init__(self):
        super().__init__("Invalid Authorization")


class OctopusClient:
    @classmethod
    async def create(cls, api_key: str, base_url: str = None):
        self = OctopusClient(api_key, base_url)
        return await self.login()

    def __init__(self, api_key: str, account_number: str, base_url: str = None):
        self.base_url = "https://api.octopus.energy" if base_url is None else base_url
        basic_auth = BasicAuth(login=api_key, password="")
        self.authenticated_session = aiohttp.ClientSession(auth=basic_auth)
        self.session = aiohttp.ClientSession()
        self.account_number = account_number

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()

    async def close(self):
        await self.authenticated_session.close()
        await self.session.close()

    async def get_account(self) -> Account:
        resp = await self.__get_athenticated(f"v1/accounts/{self.account_number}/")
        body = await resp.json()
        account = Account.model_validate(body)
        return account

    async def get_agile_prices(
        self,
        product_code: str,
        tariff_code: str,
        period_from: Optional[datetime] = None,
        period_to: Optional[datetime] = None,
        page: Optional[int] = None,
    ) -> Rates:
        params = urlencode(
            clean_nones(
                {"period_from": period_from.strftime('%Y-%m-%dT%H:%MZ') or period_from, "period_to": period_to.strftime('%Y-%m-%dT%H:%MZ') or period_to, "page": page}
            ), safe=':+'
        )
        print(f"params: {params}")
        print(
            f"v1/products/{product_code}/electricity-tariffs/{tariff_code}/standard-unit-rates/"
            + f"?{params}"
            if len(params) > 0
            else ""
        )

        resp = await self.__get(
            f"v1/products/{product_code}/electricity-tariffs/{tariff_code}/standard-unit-rates/"
            + f"?{params}"
            if len(params) > 0
            else ""
        )
        body = await resp.json()

        print(f"body: {body}")

        rates = Rates.model_validate(body)

        print(f"rates: {rates}")

        return rates

    async def __get_athenticated(self, path: str, attempts: int = 1):
        print(f"Account path: {self.__url(path)}")
        resp = await self.authenticated_session.get(
            self.__url(path), headers=self.__headers(), timeout=20
        )
        if resp.status == 401 and attempts == 1:
            print(f"Account number: {self.__headers()}")
            raise InvalidCredentialsException()
        return resp

    async def __get(self, path: str, attempts: int = 1):
        resp = await self.session.get(
            self.__url(path), headers=self.__headers(), timeout=20
        )
        if resp.status == 401 and attempts == 1:
            raise InvalidCredentialsException()
        return resp

    def __headers(self) -> dict[str, str]:
        headers = {"Content-Type": "application/json"}
        return headers

    def __url(self, path: str) -> str:
        return f"{self.base_url}/{path}"

    def extract_product_code(self, tariff_code):
        utility = (
            "electricity"
            if tariff_code.startswith("E")
            else "gas"
            if tariff_code.startswith("G")
            else None
        )
        if not utility:
            raise Exception(f"Tariff code is not electricity or gas: {tariff_code}")
        product_code = "-".join(tariff_code.split("-")[2:-1])
        return product_code, utility
