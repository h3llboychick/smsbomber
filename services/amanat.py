from .base import Service

class Amanat(Service):
	timeout = 180
	name = "amanat24.kz"
	def format_number(phone):
		return phone	
	async def send_one(self, phone, session):	
		data = {"phone_number":self.format_number(phone),"term_of_use":"true","tracker":{"session_id":"8a5977b2-acee-40cb-ac55-4d553dcc8578","utm_parameters":{"utm_source":"false","utm_medium":"false","utm_campaign":"false","utm_term":"false"}}}	
		return await self.make_request(session, url = "https://new.amanat24.amanat.systems/api/auth/send-code", method = "post", json = data)

if __name__ == "__main__":
	Amanat.test("+77084872859")