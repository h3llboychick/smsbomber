from .base import Service
class Ecco(Service):
	timeout = 20
	name = "ecco.kz"
	async def send_one(self, phone, session):
		data = {"phone": self.format_number("+7 (7xx) xxx-xx-xx",phone),"action": "send_sms_order"}
		return await self.make_request(session, url = "https://ecco.kz/ajax_send_sms.php", method = "post", data = data)

if __name__ == "__main__":
	Ecco.test()