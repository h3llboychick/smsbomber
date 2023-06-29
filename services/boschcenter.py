from .base import Service
class Boschcenter(Service):
	timeout = 60
	name = "boschcenter.kz"
	def format_number(phone):
		return f"+{phone[1]} ({phone[2:5]}) {phone[5:8]}-{phone[8:10]}-{phone[10:12]}"
	async def send_one(self, phone, session):
		data = {"phone": self.format_number(phone)}
		return await self.make_request(session, url = "https://boschcenter.kz/index.php?route=extension/module/sms_reg/SmsCheck", method = "post", data = data)

if __name__ == "__main__":
	Boschcenter.test("+77084872859")