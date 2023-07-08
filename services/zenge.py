from .base import Service
class Zenge(Service):
	timeout = 30
	name = "zenge.kz"
	async def send_one(self, phone, session):	
		return await self.make_request(session, url = f"https://zenge.kz/auth/claim_sms_with_code?phone={self.format_number('+7 (7xx) xxx-xx-xx', phone)}&procedure=reg&name=xdxd&city=1&email=", method = "get")

if __name__ == "__main__":
	Zenge.test()