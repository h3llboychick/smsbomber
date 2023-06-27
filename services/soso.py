from .base import Service
class Soso(Service):
	timeout = 30
	name = "soso.kz"
	def format_number(phone):
		return phone
	@Service.log	
	async def send_one(self, phone, session):
		data = {
			"amount": "50000",
			"phone": self.format_number(phone),
			"locale": "ru"
		}
		status, text = await self.make_request(session, url = "https://www.soso.kz/api/landing-form", data = data)	
		return (status, text)

if __name__ == "__main__":
	Soso.test("+77084872859")