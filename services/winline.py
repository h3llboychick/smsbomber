from .base import Service
import aiohttp
import asyncio
class Winline(Service):
	timeout = 60
	name = "winline.kz"
	def format_number(phone):
		return phone
	@Service.log	
	async def send_one(self, phone, session):
		data = {"phone":self.format_number(phone),"languageId":3}
		status, text = await Service.make_request(session, url = "https://winline.kz/api/kaz/registration/send-sms-code", method = "post", json = data)
		return (status, text)

if __name__ == "__main__":
	Winline.test("+77084872859")