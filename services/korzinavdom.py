from .base import Service

class Korzinavdom(Service):
	timeout = 60
	name = "korzinavdom.kz"
	def format_number(phone):
		return f"{phone[1::]}"	
	async def send_one(self, phone, session):
		json = {"phone": Korzinavdom.format_number(phone)}
		return await self.make_request(session, url = "https://api.korzinavdom.kz/client/auth/smsRequest", json = json)


if __name__ == "__main__":
	Korzinavdom.test("+77084872859")