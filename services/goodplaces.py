from .base import Service

class Goodplaces(Service):
	timeout = 60
	name = "goodplaces.kz"
	allowed_statuses = [200,300]
	async def send_one(self, phone, session):
		data={"name": "Lol", "phone": self.format_number('+77xxxxxxxxx', phone)}
		return await self.make_request(session, url = "https://api.goodplaces.kz/api/v2/users/", method = "post", data = json)

if __name__ == "__main__":
	Goodplaces.test()