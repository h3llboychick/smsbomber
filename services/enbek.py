from .base import Service
class Enbek(Service):
	timeout = 30
	name = "enbek.kz"
	def format_number(phone):
		return f"+{phone[1]} ({phone[2:5]}) {phone[5:8]} {phone[8:10]} {phone[10:12]}"
	@Service.log	
	async def send_one(self, phone, session):
		data = {"phone": Enbek.format_number(phone)}
		status, text = await self.make_request(session, url = "https://passport.enbek.kz/api/ru/user/register/check-phone", data = data)	
		return (status, text)

if __name__ == "__main__":
	Enbek.test("+77084872859")