from .base import Service

class Lol3(Service):
	timeout = 30
	name = "lol3.kz"
	allowed_statuses = [200,300]
	async def send_one(self, phone, session):
		
		return await self.make_request(session, url = https://lol.kz/?phone=$phone, method = "post")

if __name__ == "__main__":
	Lol3.test()