from .base import Service
class Soso(Service):
	timeout = 30
	name = "soso.kz"
	async def send_one(self, phone, session):
		data = {"amount": "50000","phone": phone,"locale": "ru"}
		return await self.make_request(session, url = "https://www.soso.kz/api/landing-form", data = data)	
if __name__ == "__main__":
	Soso.test()