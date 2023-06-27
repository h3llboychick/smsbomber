from .base import Service
import aiohttp
import asyncio
class Kino(Service):
	timeout = 60
	name = "kino.kz"
	def format_number(phone):
		return phone[1::]
	@Service.log	
	async def send_one(self, phone, session):
		data = {"phone":self.format_number(phone),"email":""}
		status, text = await Service.make_request(session, url = "https://api.kino.kz/auth/v2/register", method = "post", json = data)
		return (status, text)

if __name__ == "__main__":
	Kino.test("+77084872859")