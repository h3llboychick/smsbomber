from base import Service
import asyncio
import aiohttp
import json
async def main():
	async with aiohttp.ClientSession() as session:
		data = {"phone":"+7 (708) 487 2859","documents":[{"name":"ClientAgreements","template":"71"},{"name":"AgreementForTakeMicrocredit","template":"73"},{"name":"LoanContract","template":"77"}]}
		status, text = await Service.make_request(session, url = "https://api.acredit.kz/user/get-token", method = "post", json = data)

		print(status, json.loads(text))

if __name__ == "__main__":
	asyncio.run(main())