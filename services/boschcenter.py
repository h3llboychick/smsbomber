from .base import Service
class Boschcenter(Service):
	timeout = 60
	name = "boschcenter.kz"
	async def send_one(self, phone, session):
		data = {"phone": self.format_number("+7 (7xx) xxx-xx-xx",phone)}
		return await self.make_request(session, url = "https://boschcenter.kz/index.php?route=extension/module/sms_reg/SmsCheck", method = "post", data = data)

if __name__ == "__main__":
	Boschcenter.test()