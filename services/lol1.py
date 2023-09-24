from .base import Service

class Lol1(Service):
	timeout = 30
	name = "lol1.kz"
	allowed_statuses = [200,300]
	async def send_one(self, phone, session):
		
		return await self.make_request(session, url = f"https://lol.kz/phone={self.format_number('+7 (7xx) xxx-xx-xx', phone)}", method = "post")

if __name__ == "__main__":
	Lol1.test()