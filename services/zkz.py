from .base import Service
class Zkz(Service):
	allowed_statuses = [500]
	timeout = 60
	name = "zkz.kz"
	async def send_one(self, phone, session):
		return await self.make_request(session, url = f"https://zkz.kz/?action=user_get_sms&login={self.format_number('+7(7xx)xxx-xx-xx', phone)}", method = "get")	

if __name__ == "__main__":
	Zkz.test()