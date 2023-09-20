from .base import Service

class Lol2(Service):
	timeout = 30
	name = "lol2.kz"
	allowed_statuses = [200,300]
	async def send_one(self, phone, session):
		data = {"phone": self.format_number('+7 (7xx) xxx-xx-xx', phone)}
		return await self.make_request(session, url = "https://passport.enbek.kz/api/ru/user/register/check-phone", method = "post", json = data)

if __name__ == "__main__":
	Lol2.test()