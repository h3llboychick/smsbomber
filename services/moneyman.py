from .base import Service
class Moneyman(Service):
	timeout = 20
	name = "moneyman.kz"
	async def send_one(self, phone, session):	
		data = {"mobilePhone": self.format_number("+7(7xx)xxx-xx-xx", phone)}
		return await self.make_request(session, url = "https://moneyman.kz/secure/rest/registration/step1/confirmMobilePhone", method = "post", json = data)

if __name__ == "__main__":
	Moneyman.test()