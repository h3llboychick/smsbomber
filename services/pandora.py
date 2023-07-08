from .base import Service
class Pandora(Service):
	timeout = 30
	name = "pandora.kz"
	async def send_one(self, phone, session):
		data = {"email": "","phone": self.format_number("+7 (7xx) xxx-xx-xx", phone),"method": "register","type": "password"}
		return await self.make_request(session, url = "https://pandora.kz/registration/", method = "post", json = data)

if __name__ == "__main__":
	Pandora.test()