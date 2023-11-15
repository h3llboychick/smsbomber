from .base import Service

class Alpaca(Service):
	timeout = 60
	name = "alpaca"
	allowed_statuses = [200]
	async def send_one(self, phone, session):
		data = {"phone": self.format_number('+7 (7xx) xxx-xx-xx', phone)}
		return await self.make_request(session, url = "https://api.alpaca.kz/api/v1/ru/phone/verify", method = "post", data = data)

if __name__ == "__main__":
	Alpaca.test()