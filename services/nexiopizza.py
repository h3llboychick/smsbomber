from .base import Service

class Nexiopizza(Service):
	name = "nexxiopizza.kz"
	timeout = 60
	async def send_one(self, phone, session):
		data = {"Login": self.format_number("+7(7xx) xxx-xx-xx", phone), "City_id": "6"}
		return await self.make_request(session, url = "https://nexxiopizza.kz/ajax/?mode=logon1", data = data)

if __name__ == "__main__":
	Nexiopizza.test()