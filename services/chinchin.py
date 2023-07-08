from .base import Service
class Chinchin(Service):
	timeout = 30
	name = "chinchin.kz"
	async def send_one(self, phone, session):
		data = {"phone": self.format_number("+7(7xx) xxx-xxxx", phone),"t": "ss"}
		return await self.make_request(session, url = "https://chinchin.kz/ajax/sms.php", data = data)	
if __name__ == "__main__":
	Chinchin.test()