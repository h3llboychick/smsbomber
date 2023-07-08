from .base import Service
class Enbek(Service):
	timeout = 30
	name = "enbek.kz"
	async def send_one(self, phone, session):
		data = {"phone": Enbek.format_number("+7 (7xx) xxx-xx-xx", phone)}
		return await self.make_request(session, url = "https://passport.enbek.kz/api/ru/user/register/check-phone", data = data)	

if __name__ == "__main__":
	Enbek.test()