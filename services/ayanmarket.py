from .base import Service
import aiohttp
import asyncio
class Ayanmarket(Service):
	timeout = 20
	name = "ayanmarket.kz"
	def format_number(phone):
		return phone
	@Service.log	
	async def send_one(self, phone, session):
		data = {"name":"","surname":"","phone":self.format_number(phone)}
		status, text = await Service.make_request(session, url = "https://ayanmarketapi.kz/api/site/client/code", method = "post", json = data)
		return (status, text)

if __name__ == "__main__":
	Ayanmarket.test("+77084872859")