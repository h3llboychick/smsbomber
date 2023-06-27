from abc import ABC, abstractmethod 
import asyncio 
import aiohttp
from loguru import logger
import sys


class Service(ABC):
	def log(func):
		async def make(self, phone, session: aiohttp.ClientSession): 
			status, text = await func(self, phone, session)
			if status in (200, 500, 400, 204):
				logger.bind(service = self.name).info(f"OK.")
			else:
				logger.bind(service = self.name, error = text).error(f"{status} HTTP error")
			return status, text
		return make
	@classmethod
	async def send_sms(self, phone):
		async with aiohttp.ClientSession() as session:
			while True:
				status, text = await self.send_one(self, phone, session)	
				if status not in (200, 500, 400, 204):
					break	
				await asyncio.sleep(self.timeout)
	@classmethod	
	def test(self, phone):
		async def make_test():
			async with aiohttp.ClientSession() as session:
				await self.send_one(self, phone, session)
		asyncio.run(make_test())				
	@abstractmethod
	async def send_one(self, phone, session):
		pass	
	@classmethod	
	async def make_request(self, session, url = "", method = "post", data = {}, json = {}, headers = {}):
		headers.update({"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"})
		if method == "post":
			if json == {}:
				async with session.post(url, data = data, headers = headers) as response:
					text = await response.text(encoding = "utf-8")
					return (response.status, text)
			else:
				async with session.post(url, json = json, headers = headers) as response:
					text = await response.text(encoding = "utf-8")
					return (response.status, text)
		elif method == "get":
			if json == {}:
				async with session.get(url, data = data, headers = headers) as response:
					text = await response.text(encoding = "utf-8")
					return (response.status, text)
			else:
				async with session.get(url, json = json, headers = headers) as response:
					text = await response.text(encoding = "utf-8")
					return (response.status, text)
		else:
			print(f"Error - method {method} is unsupported.")

	@classmethod	
	@abstractmethod
	def format_number(phone):
		pass
