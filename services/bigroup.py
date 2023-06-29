from .base import Service
class Bigroup(Service):
	timeout = 60
	name = "bi.group"
	def format_number(phone):
		return phone
	async def send_one(self, phone, session):
		data = {"phoneNumber": self.format_number(phone), "smsType": "0"}
		return await self.make_request(session, url = "https://apigw.bi.group/client-identity/api/v1.0/Sms/SendSms", method = "post", json = data)

if __name__ == "__main__":
	Bigroup.test("+77084872859")