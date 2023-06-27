from .base import Service
import aiohttp
import asyncio
class Qfilm(Service):
	timeout = 60
	name = "qfilms.kz"
	def format_number(phone):
		return f"{phone[1::]}"
	@Service.log	
	async def send_one(self, phone, session):
		data = {"phone": Qfilm.format_number(phone)}
		status, text = await self.make_request(session, url = "https://qfilm.platform24.tv/v2/otps", data = data)	
		
		return (status, text)

if __name__ == "__main__":
	Qfilm.test("+77051625076")