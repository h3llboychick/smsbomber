from .base import Service

class Lol5(Service):
	timeout = 30
	name = "lol5.kz"
	allowed_statuses = [200,300]
	async def send_one(self, phone, session):
		
		return await self.make_request(session, url = f"https://lol4.kz/phone", method = "post")

if __name__ == "__main__":
	Lol5.test()