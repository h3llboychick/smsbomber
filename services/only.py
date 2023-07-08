from .base import Service
class Only(Service):
	timeout = 60
	name = "only.kz"
	async def send_one(self, phone, session):
		data = {"phone":self.format_number("+77xxxxxxxxx", phone),"code":"","name":"","_method":"POST"}
		return await self.make_request(session, url = "https://admin.only.kz/api/auth/code/", data = data)	

if __name__ == "__main__":
	Only.test()