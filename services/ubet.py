from .base import Service
class Ubet(Service):
	timeout = 60
	name = "ubet.kz"
	async def send_one(self, phone, session):
		data = {"phone":self.format_number("77xxxxxxxxx", phone),"agreement":1}
		return await self.make_request(session, url = "https://backend.ubet.kz/auth/agreement", method = "post", json = data)

if __name__ == "__main__":
	Ubet.test()