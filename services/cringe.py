from .base import Service

class Cringe(Service):
	timeout = 180
	name = "cringe.kz"
	allowed_statuses = [200,300]
	async def send_one(self, phone, session):
		
		return await self.make_request(session, url = "f'https://api.dom.kz/api/auth/phone={self.format_number('+77xxxxxxxxx', phone)}'", method = "post")

if __name__ == "__main__":
	Cringe.test()