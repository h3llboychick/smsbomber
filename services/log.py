from .base import Service

class Log(Service):
	timeout = 30
	name = "log.kz"
	allowed_statuses = [200,300]
	async def send_one(self, phone, session):
		data = 
		return await self.make_request(session, url = "https://log.kz/?phone=$phone", method = "post", json = data)

if __name__ == "__main__":
	Log.test()