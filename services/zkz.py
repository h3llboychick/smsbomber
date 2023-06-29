from .base import Service
class Zkz(Service):
	allowed_statuses = [500]
	timeout = 60
	name = "zkz.kz"
	def format_number(phone):
		return f"+{phone[1]}({phone[2:5]}){phone[5:8]}-{phone[8:10]}-{phone[10:12]}"
	async def send_one(self, phone, session):
		return await self.make_request(session, url = f"https://zkz.kz/?action=user_get_sms&login={Zkz.format_number(phone)}", method = "get")	

if __name__ == "__main__":
	Zkz.test("+77084872859")