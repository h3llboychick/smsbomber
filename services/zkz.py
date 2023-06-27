from .base import Service
import asyncio

class Zkz(Service):
	timeout = 60
	name = "zkz.kz"
	def format_number(phone):
		return f"+{phone[1]}({phone[2:5]}){phone[5:8]}-{phone[8:10]}-{phone[10:12]}"
	@Service.log	
	async def send_one(self, phone, session):
		status, text = await self.make_request(session, url = f"https://zkz.kz/?action=user_get_sms&login={Zkz.format_number(phone)}", method = "get")	
		return (status, text)

if __name__ == "__main__":
	Zkz.test("+77084872859")