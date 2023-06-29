from abc import ABC, abstractmethod 
import asyncio 
import aiohttp
from .utils import log, configure_logs

class Service(ABC):
	allowed_methods = ["post", "get"]
	allowed_statuses = [200]
	name = None

	@classmethod	
	@abstractmethod
	def format_number(phone: str) -> str:
		pass
	
	@classmethod	
	@log
	async def make_request(self, session: aiohttp.ClientSession, url:str = "", method: str = "post", data: dict = None, json: dict = None, headers: dict = {}) -> tuple:
		headers.update({"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"})
		if method not in self.allowed_methods:
			return (404, f"Error - method {method} is unsupported.")
		else:
			async with session.request(method, url, json = json, data = data, headers = headers) as response:
				text = None
				if "application/json" in response.content_type:
					text = await response.json(encoding = "utf-8")
				else:
					text = await response.text(encoding = "utf-8")
					text = " ".join(text.replace("\r", "").split("\n"))
				status = response.status
			return (status, text)
	@abstractmethod
	async def send_one(self, phone: str, session: aiohttp.ClientSession) -> tuple:
		pass	

	@classmethod
	async def send_sms(self, phone: str) -> None:
		async with aiohttp.ClientSession() as session:
			while True:
				status = await self.send_one(self, phone, session)	
				if status not in self.allowed_statuses:
					break	
				await asyncio.sleep(self.timeout)

	@classmethod	
	def test(self, phone: str) -> None:
		async def make_test():
			async with aiohttp.ClientSession() as session:
				await self.send_one(self, phone, session)
		configure_logs()
		asyncio.run(make_test())
				
