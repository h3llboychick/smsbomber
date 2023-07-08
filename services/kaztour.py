from .base import Service
class Kaztour(Service):
	timeout = 120
	name = "kaztour.kz"
	async def send_one(self, phone, session):	
		data = {"phone": self.format_number("+7 7xx xxx-xx-xx", phone)}
		return await self.make_request(session, url = "https://kaztour.kz/api/web/v2/auth/otp/phone", data = data)

if __name__ == "__main__":
	Kaztour.test()