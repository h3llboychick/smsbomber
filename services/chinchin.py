from .base import Service
import asyncio

class Chinchin(Service):
	timeout = 30
	name = "chinchin.kz"
	def format_number(phone):
		return f"+{phone[1]}({phone[2:5]}) {phone[5:8]}-{phone[8:12]}"
	@Service.log
	async def send_one(self, phone, session):
		data = {
			"phone": Chinchin.format_number(phone),
			"t": "ss"
		}
		status, text = await self.make_request(session, url = "https://chinchin.kz/ajax/sms.php", data = data)	
		return (status, text)

if __name__ == "__main__":
	Chinchin.test("+77084872859")