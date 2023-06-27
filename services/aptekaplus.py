from .base import Service
import aiohttp
import asyncio
class Aptekaplus(Service):
	timeout = 180
	name = "aptekaplus.kz"
	def format_number(phone):
		return phone
	@Service.log	
	async def send_one(self, phone, session):	
		data = {"username": self.format_number(phone)}
		status, text = await self.make_request(session, url = "https://aptekaplus.kz/api/auth/v1/code", json = data)
		return (status, text)

if __name__ == "__main__":
	Aptekaplus.test("+77084872859")