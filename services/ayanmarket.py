from .base import Service
class Ayanmarket(Service):
	timeout = 20
	name = "ayanmarket.kz"
	async def send_one(self, phone, session):
		data = {"name":"","surname":"","phone":phone}
		return await self.make_request(session, url = "https://ayanmarketapi.kz/api/site/client/code", method = "post", json = data)

if __name__ == "__main__":
	Ayanmarket.test()