import asyncio
import os

from sunsynk.client import SunsynkClient
from dotenv import load_dotenv


async def main():
    # Load the environment variables from the .env file
    load_dotenv()

    sunsynk_username = os.getenv("SUNSYNK_USERNAME")
    sunsynk_password = os.getenv("SUNSYNK_PASSWORD")

    async with SunsynkClient(
        sunsynk_username, sunsynk_password, "https://api.sunsynk.net"
    ) as client:
        gateways = await client.get_gateways()
        inverters = await client.get_inverters()
        for inverter in inverters:
            grid = await client.get_inverter_realtime_grid(inverter.sn)
            battery = await client.get_inverter_realtime_battery(inverter.sn)
            solar_pv = await client.get_inverter_realtime_input(inverter.sn)

            output = await client.get_inverter_realtime_output(inverter.sn)

            print(
                f"Inverter (sn: {inverter.sn}) is drawing {grid.get_power()}kWh from the grid, {battery.power}kWh from battery and {solar_pv.get_power()}kWh. {output.vip}"
            )
            # print(f"Inverter (sn: {inverter.sn}) {battery.power}kWh from battery.")

        for gateway in gateways:
            print(f"Gateway (sn: {gateway.sn})")

        notifications = await client.get_notifications()

        for notification in notifications:
            print(
                f"Notification (desc: {notification.description} {notification.id} {notification.start_time} {notification.sn} {notification.start_time} {notification.soc})"
            )

    print("Done!")


asyncio.run(main())
