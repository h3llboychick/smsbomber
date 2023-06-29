from .base import Service
class Prosklad(Service):
	timeout = 60
	name = "prosklad.kz"
	def format_number(phone):
		return phone[1::]	
	async def send_one(self, phone, session):
		data = {"phone_number":self.format_number(phone)}
		return await self.make_request(session, url = "https://prosklad.kz/api/v1/register/send/confirmed-code", method = "post", json = data)

if __name__ == "__main__":
	Prosklad.test("+77084872859")