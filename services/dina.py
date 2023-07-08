from .base import Service
class Dinamarket(Service):
	timeout = 60
	name = "dinamarket.kz"
	async def send_one(self, phone, session):
		data = {"key": "registration","email": "","password": "xdxd1234","password1": "xdxd1234","name": "lolcringe","tel": self.format_number("+7(7xx) xxx-xxxx",phone),"lg": "ru","city": "1","sex": "0","dr": "1990-01-01","smscode": "","ofert": "on","prm": "1649"}
		return await self.make_request(session, url = "https://dinamarket.kz/node.php?act=smssend", method = "post", data = data)

if __name__ == "__main__":
	Dinamarket.test()