from .base import Service
class Winline(Service):
	timeout = 60
	name = "winline.kz"
	def format_number(phone):
		return phone
	async def send_one(self, phone, session):
		data = {"phone":self.format_number(phone),"languageId":3}
		return await self.make_request(session, url = "https://winline.kz/api/kaz/registration/send-sms-code", method = "post", json = data)

if __name__ == "__main__":
	Winline.test("+77084872859")