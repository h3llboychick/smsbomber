from .base import Service
class Dns(Service):
	timeout = 120
	name = "dns.kz"
	async def send_one(self, phone, session):	
		data = {"FastAuthorizationLoginLoadForm[login]": self.format_number("77xxxxxxxxx", phone),"FastAuthorizationLoginLoadForm[token]": "","FastAuthorizationLoginLoadForm[isPhoneCall]": "0"}
		return await self.make_request(session, url = "https://www.dns-shop.kz/auth/auth/fast-authorization/", method = "post", data = data)

if __name__ == "__main__":
	Dns.test()