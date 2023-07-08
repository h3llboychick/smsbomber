from .base import Service
class Enjoy(Service):
	timeout = 60
	name = "enjoydoner.kz"
	async def send_one(self, phone, session):
		data = {"phone":self.format_number("77xxxxxxxxx", phone)}
		return await self.make_request(session, url = "https://enjoy-doner.eatery.club/site/v1/pre-login", method = "post", json = data)

if __name__ == "__main__":
	Enjoy.test()