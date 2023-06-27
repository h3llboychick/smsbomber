from .base import Service
import aiohttp
import asyncio
class Sxodim(Service):
	timeout = 60
	name = "sxodim.com"
	def format_number(phone):
		return phone
	@Service.log	
	async def send_one(self, phone, session):
		data = {"city_id": 1, "phone": Sxodim.format_number(phone)}
		status, text = await self.make_request(session, url = "https://sxodim.com/api/auth/sms-code", data = data)	
		return (status, text)

if __name__ == "__main__":
	Sxodim.test("+77084872859")