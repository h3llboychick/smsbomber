from .base import Service
class Dinamarket(Service):
	timeout = 60
	name = "dinamarket.kz"
	def format_number(phone):
		return f"+{phone[1]}({phone[2:5]}) {phone[5:8]}-{phone[8:12]}"
	async def send_one(self, phone, session):
		data = {"key": "registration","email": "","password": "xdxd1234","password1": "xdxd1234","name": "lolcringe","tel": self.format_number(phone),"lg": "ru","city": "1","sex": "0","dr": "1990-01-01","smscode": "","ofert": "on","prm": "1649"}
		return await Service.make_request(session, url = "https://dinamarket.kz/node.php?act=smssend", method = "post", data = data)

if __name__ == "__main__":
	Dinamarket.test("+77084872859")