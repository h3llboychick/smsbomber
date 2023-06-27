from .base import Service
import aiohttp
import asyncio
class Lombardb(Service):
	timeout = 30
	name = "lombard-cabinet.kz"
	def format_number(phone):
		return phone[2::]
	@Service.log	
	async def send_one(self, phone, session):
		data = {"login":self.format_number(phone)} 
		status, text = await Service.make_request(session, url = "https://api.lombard-cabinet.kz/user/get_sms", method = "post", json = data)
		return (status, text)

if __name__ == "__main__":
	Lobmardb.test("+77084872859")