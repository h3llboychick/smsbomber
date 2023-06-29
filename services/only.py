from .base import Service
class Only(Service):
	timeout = 60
	name = "only.kz"
	def format_number(phone):
		return f"+{phone[1::]}"
	async def send_one(self, phone, session):
		data = {"phone":Only.format_number(phone),"code":"","name":"","_method":"POST"}
		return await self.make_request(session, url = "https://admin.only.kz/api/auth/code/", data = data)	

if __name__ == "__main__":
	Only.test("+77084872859")