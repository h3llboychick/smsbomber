from .base import Service
class Tau24(Service):
	timeout = 60
	name = "tau24.kz"
	def format_number(phone):
		return f"+{phone[1]} ({phone[2:5]}) {phone[5:8]}-{phone[8:10]}-{phone[10:12]}"	
	async def send_one(self, phone, session):
		data = {"action":"auth","data":{"type":"send_sms","phone":self.format_number(phone)}}
		return await self.make_request(session, url = "https://tau24.kz/api/ajax/", method = "post", json = data)

if __name__ == "__main__":
	Tau24.test("+77084872859")