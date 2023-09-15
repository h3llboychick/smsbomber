from .base import Service
class Yans(Service):
	timeout = 60
	name = "yans.kz"	
	async def send_one(self, phone, session):
		data = {"FORM": "SEND_CODE", "PHONE": self.format_number("+7 (7xx) xxx-xx-xx", phone)}
		return await self.make_request(session, url = "https://yans.kz/ajax/phoneAuth.php", method = "post", data = data)

if __name__ == "__main__":
	Yans.test()
