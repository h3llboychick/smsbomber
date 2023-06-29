from .base import Service
class Kupipolis(Service):
	timeout = 30
	name = "kupipolis.kz"
	def format_number(phone):
		return phone[1::]
	async def send_one(self, phone, session):
		data = {"phone_number":"77084872859"} 
		return await self.make_request(session, url = "https://kupipolis.kz/api/authorization/request-verification-code", method = "post", json = data)

if __name__ == "__main__":
	Kupipolis.test("+77084872859")