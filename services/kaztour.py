from .base import Service
class Kaztour(Service):
	timeout = 120
	name = "kaztour.kz"
	def format_number(phone):
		return f"+{phone[1]} {phone[2:5]} {phone[5:8]}-{phone[8:10]}-{phone[10:12]}"
	async def send_one(self, phone, session):	
		data = {"phone": self.format_number(phone)}
		return await self.make_request(session, url = "https://kaztour.kz/api/web/v2/auth/otp/phone", data = data)

if __name__ == "__main__":
	Kaztour.test("+77084872859")