from .base import Service
class Muzzone(Service):
	timeout = 30
	name = "muzzone.kz"
	def format_number(phone):
		return phone[1::]
	async def send_one(self, phone, session):
		return await self.make_request(session, url = f"https://muzzone.kz/index.php?dispatch=profiles.cp_phone_verification&otp_type=register&obj_id=&phone={self.format_number(phone)}&result_ids=phone_verification_&skip_result_ids_check=true&is_ajax=1", method = "get")

if __name__ == "__main__":
	Muzzone.test("+77084872859")