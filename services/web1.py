from .base import Service

class Web1(Service):
	timeout = 30
	name = "web1.com"
	allowed_statuses = [200,300,400,404]
	async def send_one(self, phone, session):
		
		return await self.make_request(session, url = f"https://web.com/?phone={self.format_number('+7 (7xx) xxx-xx-xx', phone)}", method = "post")

if __name__ == "__main__":
	Web1.test()