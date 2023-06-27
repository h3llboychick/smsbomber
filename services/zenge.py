from .base import Service
import aiohttp
import asyncio
import json
class Zenge(Service):
	timeout = 30
	name = "zenge.kz"
	def format_number(phone):
		return f"+{phone[1]} ({phone[2:5]}) {phone[5:8]}-{phone[8:10]}-{phone[10:12]}"
	@Service.log	
	async def send_one(self, phone, session):	
		status, text = await Service.make_request(session, url = f"https://zenge.kz/auth/claim_sms_with_code?phone={self.format_number(phone)}&procedure=reg&name=xdxd&city=1&email=", method = "get")
		return (status, text)

if __name__ == "__main__":
	Zenge.test("+77084872859")