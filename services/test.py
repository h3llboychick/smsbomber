from base import Service
import aiohttp
import asyncio


async def main():
	async with aiohttp.ClientSession() as session:
		data = {"name":"xdxd","middlename":"xdxd","surname":"xdxd","phone":"+7 708 487-28-59","email":"ganaf28111@fulwark.com","pass":"8G!!wAtycJbr6Bb","passRepeat":"8G!!wAtycJbr6Bb","agree":"true"}
		status, text = await Service.make_request(session, url = "https://lk.ponyexpress.ru/api/v1/createuser", method = "post", json = data)
		print(status, text)
if __name__ == "__main__":
	asyncio.run(main())