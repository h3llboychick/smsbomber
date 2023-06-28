from .base import Service
import aiohttp
import asyncio
class Muzzone(Service):
	timeout = 30
	name = "muzzone.kz"
	def format_number(phone):
		return phone[1::]
	@Service.log	
	async def send_one(self, phone, session):
		status, text = await Service.make_request(session, url = f"https://muzzone.kz/index.php?dispatch=profiles.cp_phone_verification&otp_type=register&obj_id=&phone={self.format_number(phone)}&result_ids=phone_verification_&skip_result_ids_check=true&is_ajax=1", method = "get")
		return (status, text)

if __name__ == "__main__":
	Muzzone.test("+77084872859")