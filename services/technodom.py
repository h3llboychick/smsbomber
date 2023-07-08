from .base import Service
class Technodom(Service):
	timeout = 60
	name = "technodom.kz"
	async def send_one(self, phone, session):	
		json = {"phone": self.format_number("77xxxxxxxxx", phone)}
		return await self.make_request(session, url = "https://sso.technodom.kz/api/v1/events/verify/phone", method = "post", json = json)

if __name__ == "__main__":
	Technodom.test()