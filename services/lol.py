from .base import Service

class Lol(Service):
	timeout = 30
	name = "lol.kz"
	allowed_statuses = [200,300]
	async def send_one(self, phone, session):
		data = {"phone": self.format_number('+7 (7xx) xxx-xx-xx', phone)}
		return await self.make_request(session, url = 'https://lol.kz/phone', method = "post", data = data)

if __name__ == "__main__":
	Lol.test()