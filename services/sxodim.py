from .base import Service
class Sxodim(Service):
	timeout = 60
	name = "sxodim.com"
	def format_number(phone):
		return phone	
	async def send_one(self, phone, session):
		data = {"city_id": 1, "phone": Sxodim.format_number(phone)}
		return await self.make_request(session, url = "https://sxodim.com/api/auth/sms-code", data = data)	

if __name__ == "__main__":
	Sxodim.test("+77084872859")