from .base import Service

class Enbek2(Service):
	timeout = 60
	name = "enbek2.kz"
	allowed_statuses = [200,300,400]
	async def send_one(self, phone, session):
		
		return await self.make_request(session, url = f"https://passport.enbek.kz/api/ru/user/register/phone={self.format_number('+7 (7xx) xxx-xx-xx', phone)}", method = "post")

if __name__ == "__main__":
	Enbek2.test()