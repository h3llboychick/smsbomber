from .base import Service
class Kupipolis(Service):
	timeout = 30
	name = "kupipolis.kz"
	async def send_one(self, phone, session):
		data = {"phone_number": self.format_number("77xxxxxxxxx", phone)} 
		return await self.make_request(session, url = "https://kupipolis.kz/api/authorization/request-verification-code", method = "post", json = data)

if __name__ == "__main__":
	Kupipolis.test()