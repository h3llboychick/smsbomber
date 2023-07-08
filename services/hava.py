from .base import Service
class Hava(Service):
	timeout = 120
	name = "hava.kz"
	async def send_one(self, phone, session):	
		data = {"mobilePhone":{"number":self.format_number("7xxxxxxxxx",phone)}}
		return await self.make_request(session, url = "https://api.hava.credit/web/public/client/phone/sms-code", method = "post", json = data)

if __name__ == "__main__":
	Hava.test()