from .base import Service
import aiohttp
import asyncio
import json
class Technodom(Service):
	timeout = 60
	name = "technodom.kz"
	def format_number(phone):
		return f"{phone[1::]}"
	@Service.log	
	async def send_one(self, phone, session):	
		json = {
			"phone": self.format_number(phone)
		}
		status, text = await Service.make_request(session, url = "https://sso.technodom.kz/api/v1/events/verify/phone", method = "post", json = json)
		return (status, text)

if __name__ == "__main__":
	Technodom.test("+77084872859")