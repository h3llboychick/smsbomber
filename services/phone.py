from .base import Service

class Phone(Service):
	timeout = 60
	name = "phone.com"
	allowed_statuses = [200,300]
	async def send_one(self, phone, session):
		
		return await self.make_request(session, url = ""f"https://phone.com/phone={self.format_number('+77xxxxxxxxx', phone)}", method = "post")

if __name__ == "__main__":
	Phone.test()