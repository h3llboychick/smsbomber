from .base import Service
import aiohttp
import asyncio
import json
class Moneyman(Service):
	timeout = 20
	name = "moneyman.kz"
	def format_number(phone):
		return f"+{phone[1]}({phone[2:5]}){phone[5:8]}-{phone[8:10]}-{phone[10:12]}"
	@Service.log	
	async def send_one(self, phone, session):	
		data = {"mobilePhone":"+7(708)487-28-59"}
		status, text = await Service.make_request(session, url = "https://moneyman.kz/secure/rest/registration/step1/confirmMobilePhone", method = "post", json = data)
		return (status, text)

if __name__ == "__main__":
	Moneyman.test("+77084872859")