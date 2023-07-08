from .base import Service
class Lenstore(Service):
	timeout = 60
	name = "lenstore.kz"
	async def send_one(self, phone, session):
		return await self.make_request(session, url = f"https://admin.lenstore.kz/api/v1/auth/signin?phone={self.format_number('77xxxxxxxxx', phone)}", method = "get")
		
if __name__ == "__main__":
	Lenstore.test()