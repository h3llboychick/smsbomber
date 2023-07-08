from .base import Service
class Basel(Service):
	timeout = 30
	name = "basel.kz"
	async def send_one(self, phone, session):
		data = {"phone":self.format_number("+7(7xx)xxx-xx-xx", phone),"type":{"value":"phone","label":"Телефон","checked":"true","name":"verify_type"},"recovery":"false","noValidate":"false"}
		return await self.make_request(session, url = "https://www.basel.kz/api/basel/sendVerifyCode", method = "post", json = data)

if __name__ == "__main__":
	Basel.test()