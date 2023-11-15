from .base import Service
class Tssp(Service):
	timeout = 30
	name = "tssp.kz"
	async def send_one(self, phone, session):
		data = {"mobile":self.format_number("+77xxxxxxxxx", phone)}
		return await self.make_request(session, url = "https://my.tssp.kz/api/customer/v1/register-by-mobile", method = "post", json = data)

if __name__ == "__main__":
	Tssp.test()
