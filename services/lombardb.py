from .base import Service
class Lombardb(Service):
	allowed_statuses = [204]
	timeout = 30
	name = "lombard-cabinet.kz"
	def format_number(phone):
		return phone[2::]
	async def send_one(self, phone, session):
		data = {"login":self.format_number(phone)} 
		return await self.make_request(session, url = "https://api.lombard-cabinet.kz/user/get_sms", method = "post", json = data)
		
if __name__ == "__main__":
	Lombardb.test("+77084872859")