from .base import Service
import aiohttp
import asyncio
class Zeta(Service):
	timeout = 20
	name = "zeta.kz"
	def format_number(phone):
		return phone[2::]
	@Service.log	
	async def send_one(self, phone, session):
		data = {"phone": "7084872859"}
		status, text = await Service.make_request(session, url = "https://zeta.kz/local/templates/ilab_it_shop/ilab/ajax/generation_code_for_regist.php", method = "post", data = data)
		return (status, text)

if __name__ == "__main__":
	Zeta.test("+77084872859")