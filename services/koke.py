from .base import Service
import aiohttp
import asyncio
import json
class Koke(Service):
	timeout = 120
	name = "koke.kz"
	def format_number(phone):
		return f"{phone[2::]}"
	@Service.log	
	async def send_one(self, phone, session):	
		data = {"mobilePhone":{"number":self.format_number(phone)}}
		status, text = await Service.make_request(session, url = "https://api.koke.credit/web/public/client/phone/sms-code", method = "post", json = data)
		return (status, text)

if __name__ == "__main__":
	Koke.test("+77084872859")