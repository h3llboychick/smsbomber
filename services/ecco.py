from .base import Service
import aiohttp
import asyncio
class Ecco(Service):
	timeout = 20
	name = "ecco.kz"
	def format_number(phone):
		return f"+{phone[1]} ({phone[2:5]}) {phone[5:8]}-{phone[8:10]}-{phone[10:12]}"
	@Service.log	
	async def send_one(self, phone, session):
		data = {
			"phone": self.format_number(phone),
			"action": "send_sms_order"
		}
		status, text = await Service.make_request(session, url = "https://ecco.kz/ajax_send_sms.php", method = "post", data = data)
		return (status, text)

if __name__ == "__main__":
	Ecco.test("+77084872859")