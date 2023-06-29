from .base import Service
class Pandora(Service):
	timeout = 30
	name = "pandora.kz"
	def format_number(phone):
		return f"+{phone[1]} ({phone[2:5]}) {phone[5:8]}-{phone[8:10]}-{phone[10:12]}"	
	async def send_one(self, phone, session):
		data = {"email": "","phone": self.format_number(phone),"method": "register","type": "password"}
		return await self.make_request(session, url = "https://pandora.kz/registration/", method = "post", json = data)

if __name__ == "__main__":
	Pandora.test("+77084872859")