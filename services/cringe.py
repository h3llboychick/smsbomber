from .base import Service

class Cringe(Service):
	timeout = 30
	name = "cringe.kz"
	allowed_statuses = [200,300]
	async def send_one(self, phone, session):
		
		return await self.make_request(session, url = f'https://passport.enbek.kz/api/ru/user/register/check-phone', method = "post")

if __name__ == "__main__":
	Cringe.test()