from .base import Service
class Prosklad(Service):
	timeout = 60
	name = "prosklad.kz"	
	async def send_one(self, phone, session):
		data = {"phone_number":self.format_number("77xxxxxxxxx",phone)}
		return await self.make_request(session, url = "https://prosklad.kz/api/v1/register/send/confirmed-code", method = "post", json = data)

if __name__ == "__main__":
	Prosklad.test()