from .base import Service
class Astanahub(Service):
	timeout = 60
	name = "astanahub.com"
	async def send_one(self, phone, session):
		data = {"phone": self.format_number("+77xxxxxxxxx", phone)}
		return await self.make_request(session, url = "https://astanahub.com/account/api/v2/auth/phone_registration/", method = "post", json = data)

if __name__ == "__main__":
	Astanahub.test()