from .base import Service
import aiohttp
import asyncio
import json
class Dns(Service):
	timeout = 120
	name = "dns.kz"
	def format_number(phone):
		return f"{phone[1::]}"
	@Service.log	
	async def send_one(self, phone, session):	
		data = {
					"FastAuthorizationLoginLoadForm[login]": self.format_number(phone),
					"FastAuthorizationLoginLoadForm[token]": "",
					"FastAuthorizationLoginLoadForm[isPhoneCall]": "0"
				}
		status, text = await Service.make_request(session, url = "https://www.dns-shop.kz/auth/auth/fast-authorization/", method = "post", data = data)
		return (status, text)

if __name__ == "__main__":
	Dns.test("+77084872859")