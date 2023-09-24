from .base import Service

class Enbek1(Service):
	timeout = 60
	name = "enbek1.kz"
	allowed_statuses = [200,300,400]
	async def send_one(self, phone, session):
		data = {"phone": self.format_number('+7 (7xx) xxx-xx-xx', phone)}
		return await self.make_request(session, url = 'https://passport.enbek.kz/api/ru/user/register/check-phone', method = "post", data = data)

if __name__ == "__main__":
	Enbek1.test()