from .base import Service
import aiohttp
import asyncio
class Wipon(Service):
	timeout = 60
	name = "app.wipon.pro"
	def format_number(phone):
		return phone
	@Service.log	
	async def send_one(self, phone, session):
		data = {"phone_number":"+77084872859"}
		status, text = await Service.make_request(session, url = "https://api.pro.wipon.kz/v1/auth", method = "post", json = data)
		return (status, text)

if __name__ == "__main__":
	Wipon.test("+77084872859")