from .base import Service

class Dom(Service):
	timeout = 180
	name = "dom.kz"
	allowed_statuses = [200,300]
	async def send_one(self, phone, session):
		data = {"phone": self.format_number('+77xxxxxxxxx', phone)}
		return await self.make_request(session, url = "https://api.dom.kz/api/auth/phone", method = "post", json = data)

if __name__ == "__main__":
	Dom.test()
