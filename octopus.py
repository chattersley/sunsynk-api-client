import asyncio
import os

from octopus.client import OctopusClient
from dotenv import load_dotenv
from datetime import datetime, timedelta
import pandas as pd
import logging


async def main():
    # Load the environment variables from the .env file
    load_dotenv()

    octopus_api_key = os.getenv("OCTOPUS_API_KEY")
    octopus_account_number = os.getenv("OCTOPUS_ACCOUNT_NUMBER")

    async with OctopusClient(
        octopus_api_key, octopus_account_number, "https://api.octopus.energy"
    ) as client:
        account = await client.get_account()
        print(f"Account number: {account.number}")

        agreements = pd.DataFrame.from_records(
            account.properties[0].electricity_meter_points[0].agreements,
            columns=["tariff_code", "valid_from", "valid_to"],
        )
        tariff_code = agreements.iloc[agreements["valid_to"].argmax()].loc[
            "tariff_code"
        ][1]
        print(f"tariff code: {tariff_code}")
        product = client.extract_product_code(agreements.iloc[agreements['valid_to'].argmax()].loc['tariff_code'][1])
        print(f"product: {product}")
 
        # Get today's date
        today = datetime.today().replace(hour=21, minute=0)
        print("Today is: ", today)
        
        # Yesterday date
        tomorrow = today + timedelta(days = 1)
        print("tomorrow is: ", tomorrow)

        rates = await client.get_agile_prices(product[0], tariff_code, today, tomorrow)
        print(f"rates: {rates}")

    print("Done!")


asyncio.run(main())
