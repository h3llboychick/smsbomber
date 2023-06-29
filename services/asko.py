from .base import Service
class Asko(Service):
	timeout = 180
	name = "asko.kz"
	def format_number(phone):
		return f"{phone[1::]}"		
	async def send_one(self, phone, session):	
		data = {"phone": self.format_number(phone),"lastName": "sdafsdaf","firstName": "dsdf","middleName": "sdfsdf","bornDate": "2008-06-19"}
		return await self.make_request(session, url = "https://api.asko.kz/v1/cabinet/auth", method = "post", data = data)

if __name__ == "__main__":
	Asko.test("+77084872859")