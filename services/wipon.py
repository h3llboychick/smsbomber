from .base import Service
class Wipon(Service):
	timeout = 60
	name = "app.wipon.pro"
	async def send_one(self, phone, session):
		data = {"phone_number": phone}
		return await self.make_request(session, url = "https://api.pro.wipon.kz/v1/auth", method = "post", json = data)

if __name__ == "__main__":
	Wipon.test()