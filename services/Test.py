from base import Service
import asyncio
import aiohttp
from utils import logs
from loguru import logger
import sys
async def main():
    async with aiohttp.ClientSession() as session:
        json = {"data":{"type":"checkPhone","attributes":{"phone":"+77084872859"}}}
        await Service.make_request(session, url = "https://api.tsum.ru/authorize/request-sms", json = json, method = "post")
if __name__ == "__main__":
    logs.enable_logs()
    asyncio.get_event_loop().run_until_complete(main())