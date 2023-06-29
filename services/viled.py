from .base import Service
class Viled(Service):
	timeout = 60
	name = "viled.kz"
	def format_number(phone):
		return f"{phone[1::]}"	
	async def send_one(self, phone, session):
		return await self.make_request(session, url = f"https://api-prod.viled.kz/tizilimer/api/v1/users/sms?phone={Viled.format_number(phone)}", method = "get")	

if __name__ == "__main__":
	Viled.test("+77084872859")