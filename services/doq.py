from .base import Service
class Doq(Service):
	timeout = 30
	name = "doq.kz"
	allowed_statuses = [201]
	async def send_one(self, phone, session):
		data = {"target":"client_profile","phone":self.format_number("+77xxxxxxxxx", phone)}
		return await self.make_request(session, url = "https://api.doq.kz/api/v0/registration_codes/", method = "post", json = data)

if __name__ == "__main__":
	Doq.test()