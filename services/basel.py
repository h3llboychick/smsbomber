from .base import Service
class Basel(Service):
	timeout = 30
	name = "basel.kz"
	def format_number(phone):
		return f"+{phone[1]}({phone[2:5]}){phone[5:8]}-{phone[8:10]}-{phone[10:12]}"
	
	async def send_one(self, phone, session):
		data = {"phone":self.format_number(phone),"type":{"value":"phone","label":"Телефон","checked":"true","name":"verify_type"},"recovery":"false","noValidate":"false"}
		return await Service.make_request(session, url = "https://www.basel.kz/api/basel/sendVerifyCode", method = "post", json = data)

if __name__ == "__main__":
	Basel.test("+77084872859")