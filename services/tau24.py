from .base import Service
class Tau24(Service):
	timeout = 60
	name = "tau24.kz"
	async def send_one(self, phone, session):
		data = {"action":"auth","data":{"type":"send_sms","phone":self.format_number("+7 (7xx) xxx-xx-xx", phone)}}
		return await self.make_request(session, url = "https://tau24.kz/api/ajax/", method = "post", json = data)

if __name__ == "__main__":
	Tau24.test()