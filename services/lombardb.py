from base import Service
from utils import logs
class Lombardb(Service):
	allowed_statuses = [204]
	timeout = 30
	name = "lombard-cabinet.kz"
	def format_number(phone):
		return phone[2::]
	async def send_one(self, phone, session):
		data = {"login":self.format_number(phone)} 
		status = await Service.make_request(session, url = "https://api.lombard-cabinet.kz/user/get_sms", method = "post", json = data)
		print(status)
		return status
		

if __name__ == "__main__":
	logs.enable_logs()
	Lombardb.test("+77084872859")