from .base import Service
import aiohttp
import asyncio
class Krendel(Service):
	timeout = 10
	name = "shop.krendel.kz"
	def format_number(phone):
		return f"+{phone[1]} {phone[2:5]} {phone[5:8]} {phone[8:10]} {phone[10:12]}"
	@Service.log
	async def send_one(self, phone, session):
		data = {
			"phone": Krendel.format_number(phone),
			"page": "537",
			"action": "send_sms"
		}
		status, text = await self.make_request(session, url = "https://shop.krendel.kz/", data = data)
		return (status, text)

if __name__ == "__main__":
	Krendel.test("+77084872859")