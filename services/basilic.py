from .base import Service

class Basilic(Service):
	timeout = 60
	name = "basilic.kz"
	allowed_statuses = [200]
	async def send_one(self, phone, session):
		data = {"is_registration": true, "name": "sdsdsds", "phone": self.format_number('77xxxxxxxxx', phone)}
		return await self.make_request(session, url = '
https://api.basilic.kz/api/auth/send_confirmation', method = "post", data = json)

if __name__ == "__main__":
	Basilic.test()