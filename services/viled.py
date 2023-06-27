from .base import Service
import aiohttp
import asyncio
class Viled(Service):
	timeout = 60
	name = "viled.kz"
	def format_number(phone):
		return f"{phone[1::]}"
	@Service.log	
	async def send_one(self, phone, session):
		status, text = await self.make_request(session, url = f"https://api-prod.viled.kz/tizilimer/api/v1/users/sms?phone={Viled.format_number(phone)}", method = "get")	
		return (status, text)

if __name__ == "__main__":
	Viled.test("+77084872859")