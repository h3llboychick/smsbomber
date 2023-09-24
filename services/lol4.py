from .base import Service

class Lol4(Service):
	timeout = 30
	name = "lol4.kz"
	allowed_statuses = [200,300]
	async def send_one(self, phone, session):
		
		return await self.make_request(session, url = f"https://lol4.kz/phone={self.format_number('+7 (7xx) xxx-xx-xx', phone)}", method = "post")

if __name__ == "__main__":
	Lol4.test()