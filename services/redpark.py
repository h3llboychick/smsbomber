from .base import Service
class Redpark(Service):
	timeout = 20
	name = "redpark.kz"
	def format_number(phone):
		return f"+{phone[1]} ({phone[2:5]}) {phone[5:8]}-{phone[8:10]}-{phone[10:12]}"
	async def send_one(self, phone, session):
		data = {"phone": self.format_number(phone),"type": "registration"}
		return await self.make_request(session, url = "https://redpark.kz/bitrix/services/main/ajax.php?mode=class&c=o2k%3Aphone.login&action=login", method = "post", data = data)

if __name__ == "__main__":
	Redpark.test("+77084872859")