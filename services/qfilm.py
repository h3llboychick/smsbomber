from .base import Service
class Qfilm(Service):
	timeout = 60
	name = "qfilms.kz"
	async def send_one(self, phone, session):
		data = {"phone": Qfilm.format_number("77xxxxxxxxx", phone)}
		return await self.make_request(session, url = "https://qfilm.platform24.tv/v2/otps", data = data)	

if __name__ == "__main__":
	Qfilm.test()