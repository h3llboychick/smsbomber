from .base import Service
import aiohttp
import asyncio
class Mechta(Service):
	timeout = 60
	name = "mechta.kz"
	def format_number(phone):
		return f"{phone[1::]}"
	@Service.log	
	async def send_one(self, phone, session):	
		data = {"phone": Mechta.format_number(phone), "type": "login"}
		status, text = await self.make_request(session, url = "https://www.mechta.kz/api/v2/send-sms", data = data)
		return (status, text)

if __name__ == "__main__":
	Mechta.test("+77084872859")