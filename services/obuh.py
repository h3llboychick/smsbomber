from .base import Service
class Obuh(Service):
	timeout = 180
	name = "obuhgalter.kz"
	async def send_one(self, phone, session):
		return await self.make_request(session, url = f"https://api.onlinebank.kz/authentication/get-sms/{self.format_number('7xxxxxxxxx', phone)}", method = "get")

if __name__ == "__main__":
	Obuh.test()