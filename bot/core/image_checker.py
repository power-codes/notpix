import json
import random
import aiohttp
import asyncio
from PIL import Image
from io import BytesIO
from bot.utils import logger
from tenacity import retry, wait_fixed, stop_after_attempt

async def send_request(method, url, json=None, times_to_fall=10):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, json=json, ssl=False) as response:
                response.raise_for_status() 
                return await response.json()
    except aiohttp.ClientError as e:
        logger.error(f"Network error occurred: {e}, retrying in 30 seconds, attempt {10 - times_to_fall + 1}/10")
        await asyncio.sleep(5)
        if times_to_fall > 0:
            return await send_request(method, url, json, times_to_fall - 1)
        exit()
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        exit()

async def reacheble(times_to_fall=10):
    response = await send_request("GET", "http://notpixel.powercodes.top/is_reacheble/")
    if response:
        logger.success("Connected to notpixel.powercodes.top server ")

async def participate(username, times_to_fall=10):
    response = await send_request("PUT", "http://notpixel.powercodes.top/owner_info/", json={"telegram_tag": username})
    if response:
        logger.success(f"We will write you on @{username} if you win")

async def inform(user_id, balance=None, times_to_fall=10):
    if balance is None:
        balance = 0  
    response = await send_request("PUT", "http://notpixel.powercodes.top/info/", json={"user_id": user_id, "balance": balance})
    if response:
        return response

async def get_cords_and_color(user_id, template, times_to_fall=10):
    response = await send_request("GET", f"http://notpixel.powercodes.top/get_pixel/?user_id={user_id}&template={template}")
    return response

async def template_to_join(cur_template=0, times_to_fall=10):
    response = await send_request("GET", f"http://notpixel.powercodes.top/get_uncolored/?template={cur_template}")
    if response:
        return response['template']


async def main():
    await reacheble()
    await participate("username_example")
    await inform("user_id_example", 100)
    coords_and_color = await get_cords_and_color("user_id_example", "template_example")
    template = await template_to_join()


if __name__ == "__main__":
    asyncio.run(main())
