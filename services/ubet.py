from .base import Service
import aiohttp
import asyncio
class Ubet(Service):
	timeout = 60
	name = "ubet.kz"
	def format_number(phone):
		return phone[1::]
	@Service.log	
	async def send_one(self, phone, session):
		data = {"phone":self.format_number(phone),"agreement":1}
		status, text = await Service.make_request(session, url = "https://backend.ubet.kz/auth/agreement", method = "post", json = data)
		return (status, text)

if __name__ == "__main__":
	Ubet.test("+77084872859")