from .base import Service
class Koke(Service):
	timeout = 120
	name = "koke.kz"
	def format_number(phone):
		return f"{phone[2::]}"
	async def send_one(self, phone, session):	
		data = {"mobilePhone":{"number":self.format_number(phone)}}
		return await Service.make_request(session, url = "https://api.koke.credit/web/public/client/phone/sms-code", method = "post", json = data)
		

if __name__ == "__main__":
	Koke.test("+77084872859")