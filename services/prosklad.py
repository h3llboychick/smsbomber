from .base import Service
import aiohttp
import asyncio
class Prosklad(Service):
	timeout = 60
	name = "prosklad.kz"
	def format_number(phone):
		return phone[1::]
	@Service.log	
	async def send_one(self, phone, session):
		data = {"phone_number":self.format_number(phone)}
		status, text = await Service.make_request(session, url = "https://prosklad.kz/api/v1/register/send/confirmed-code", method = "post", json = data)
		return (status, text)

if __name__ == "__main__":
	Prosklad.test("+77084872859")