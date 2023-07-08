from .base import Service
class Zeta(Service):
	timeout = 20
	name = "zeta.kz"
	async def send_one(self, phone, session):
		data = {"phone": self.format_number("7xxxxxxxxx", phone)}
		return await self.make_request(session, url = "https://zeta.kz/local/templates/ilab_it_shop/ilab/ajax/generation_code_for_regist.php", method = "post", data = data)

if __name__ == "__main__":
	Zeta.test()