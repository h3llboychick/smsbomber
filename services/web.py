from .base import Service

class Web(Service):
	timeout = 30
	name = "web.com"
	allowed_statuses = [200,300]
	async def send_one(self, phone, session):
		data = {fsfsdfsdfd}
		return await self.make_request(session, url = 'https://web.com/', method = "post", data = data)

if __name__ == "__main__":
	Web.test()