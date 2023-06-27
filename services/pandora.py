from .base import Service
import aiohttp
import asyncio
class Pandora(Service):
	timeout = 30
	name = "pandora.kz"
	def format_number(phone):
		return f"+{phone[1]} ({phone[2:5]}) {phone[5:8]}-{phone[8:10]}-{phone[10:12]}"
	@Service.log	
	async def send_one(self, phone, session):
		data = {
			"email": "",
			"phone": self.format_number(phone),
			"method": "register",
			"type": "password"
		}
		status, text = await Service.make_request(session, url = "https://pandora.kz/registration/", method = "post", json = data)
		return (status, text)

if __name__ == "__main__":
	Pandora.test("+77084872859")