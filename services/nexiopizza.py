from .base import Service

class Nexiopizza(Service):
	name = "nexxiopizza.kz"
	timeout = 60
	def format_number(phone):
		return f"+{phone[1]}({phone[2:5]}) {phone[5:8]}-{phone[8:10]}-{phone[10:12]}"
	
	async def send_one(self, phone, session):
		data = {"Login": Nexiopizza.format_number(phone), "City_id": "6"}
		return await self.make_request(session, url = "https://nexxiopizza.kz/ajax/?mode=logon1", data = data)

if __name__ == "__main__":
	Nexiopizza.test("+77084872859")