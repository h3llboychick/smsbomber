from .base import Service
class Krendel(Service):
	timeout = 10
	name = "shop.krendel.kz"
	async def send_one(self, phone, session):
		data = {"phone": Krendel.format_number("+7 7xx xxx xx xx",phone), "page": "537","action": "send_sms"}
		return await self.make_request(session, url = "https://shop.krendel.kz/", data = data)

if __name__ == "__main__":
	Krendel.test()
