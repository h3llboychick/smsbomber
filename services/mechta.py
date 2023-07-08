from .base import Service
class Mechta(Service):
	timeout = 60
	name = "mechta.kz"
	async def send_one(self, phone, session):	
		data = {"phone": self.format_number("77xxxxxxxxx", phone), "type": "login"}
		return await self.make_request(session, url = "https://www.mechta.kz/api/v2/send-sms", data = data)

if __name__ == "__main__":
	Mechta.test()