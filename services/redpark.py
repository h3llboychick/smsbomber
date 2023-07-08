from .base import Service
class Redpark(Service):
	timeout = 20
	name = "redpark.kz"
	async def send_one(self, phone, session):
		data = {"phone": self.format_number("+7 (7xx) xxx-xx-xx", phone),"type": "registration"}
		return await self.make_request(session, url = "https://redpark.kz/bitrix/services/main/ajax.php?mode=class&c=o2k%3Aphone.login&action=login", method = "post", data = data)

if __name__ == "__main__":
	Redpark.test()