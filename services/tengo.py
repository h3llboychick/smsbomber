from .base import Service
class Tengo(Service):
	timeout = 120
	name = "tengo.kz"
	def format_number(phone):
		return f"{phone[2::]}"
	async def send_one(self, phone, session):	
		data = {"mobilePhone":{"number":self.format_number(phone)}}
		return await self.make_request(session, url = "https://api.tengo.credit/web/public/client/phone/sms-code", method = "post", json = data)

if __name__ == "__main__":
	Tengo.test("+77084872859")