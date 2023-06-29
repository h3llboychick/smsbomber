from .base import Service
class Qfilm(Service):
	timeout = 60
	name = "qfilms.kz"
	def format_number(phone):
		return f"{phone[1::]}"
	async def send_one(self, phone, session):
		data = {"phone": Qfilm.format_number(phone)}
		return await self.make_request(session, url = "https://qfilm.platform24.tv/v2/otps", data = data)	

if __name__ == "__main__":
	Qfilm.test("+77084872859")