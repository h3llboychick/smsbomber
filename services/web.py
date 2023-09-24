from .base import Service

class Web(Service):
	timeout = 30
	name = "web.com"
	allowed_statuses = [200,300,400,404]
	async def send_one(self, phone, session):
		data = {"phone": self.format_number('+7 (7xx) xxx-xx-xx', phone)}
		return await self.make_request(session, url = 'https://web.com/', method = "post", data = data)

if __name__ == "__main__":
	Web.test()