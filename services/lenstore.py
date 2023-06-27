from base import Service
import aiohttp
import asyncio
class Lenstore(Service):
	timeout = 60
	name = "lenstore.kz"
	def format_number(phone):
		return f"{phone[1::]}"
	@Service.log	
	async def send_one(self, phone, session):
		status, text = await Service.make_request(session, url = f"https://admin.lenstore.kz/api/v1/auth/signin?phone={self.format_number(phone)}", method = "get")
		return (status, text)

if __name__ == "__main__":
	Lenstore.test("+77084872859")