from .base import Service

class Viled1(Service):
	timeout = 120
	name = "viled1"
	allowed_statuses = [200]
	async def send_one(self, phone, session):
		
		return await self.make_request(session, url = f"https://api-prod.viled.kz/tizilimer/api/v1/users/sms?phone={{self.format_number('77xxxxxxxxx', phone)}}", method = "get")

if __name__ == "__main__":
	Viled1.test()