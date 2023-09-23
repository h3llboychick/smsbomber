from .base import Service

class Phone1(Service):
	timeout = 60
	name = "phone1.com"
	allowed_statuses = [200,300]
	async def send_one(self, phone, session):
		data = {"phone": self.format_number('+77xxxxxxxxx', phone)}
		return await self.make_request(session, url = "https://phone.com/phone", method = "post", data = json)

if __name__ == "__main__":
	Phone1.test()