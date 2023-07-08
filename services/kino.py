from .base import Service
class Kino(Service):
	timeout = 60
	name = "kino.kz"
	async def send_one(self, phone, session):
		data = {"phone":self.format_number("77xxxxxxxxx", phone),"email":""}
		return await self.make_request(session, url = "https://api.kino.kz/auth/v2/register", method = "post", json = data)

if __name__ == "__main__":
	Kino.test()