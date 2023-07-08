from .base import Service
class Sxodim(Service):
	timeout = 60
	name = "sxodim.com"
	async def send_one(self, phone, session):
		data = {"city_id": 1, "phone": phone}
		return await self.make_request(session, url = "https://sxodim.com/api/auth/sms-code", data = data)	

if __name__ == "__main__":
	Sxodim.test()