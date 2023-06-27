from .base import Service
import aiohttp
import asyncio
class Enjoy(Service):
	timeout = 60
	name = "enjoydoner.kz"
	def format_number(phone):
		return phone[1::]
	@Service.log	
	async def send_one(self, phone, session):
		data = {"phone":self.format_number(phone)}
		status, text = await Service.make_request(session, url = "https://enjoy-doner.eatery.club/site/v1/pre-login", method = "post", json = data)
		return (status, text)

if __name__ == "__main__":
	Enjoy.test("+77084872859")