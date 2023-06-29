import asyncio
from services import Krendel, Enjoy, Zkz, Korzinavdom, Redpark, Nexiopizza, Mechta, Kino, Sxodim, Dinamarket, Ecco, Only, Viled, Dinamarket, Qfilm, Enbek, Aptekaplus, Kaztour, Chinchin, Amanat, Asko, Basel, Boschcenter, Zenge, Technodom, Dns, Koke, Moneyman, Soso, Tengo, Tomi, Lenstore, Hava, Ubet, Winline, Pandora, Kupipolis, Lombardb, Bigroup, Zeta, Tau24, Prosklad, Muzzone, Ayanmarket, Wipon
from services.utils import configure_logs
async def main(phone):
	services = [Krendel, Enjoy, Zkz, Korzinavdom, Redpark, Nexiopizza, Mechta, Kino, Sxodim, Dinamarket, Ecco, Only, Viled, Dinamarket, Qfilm, Enbek, Aptekaplus, Kaztour, Chinchin, Amanat, Asko, Basel, Boschcenter, Zenge, Technodom, Dns, Koke, Moneyman, Soso, Tengo, Tomi, Lenstore, Hava, Ubet, Winline, Pandora, Kupipolis, Lombardb, Bigroup, Zeta, Tau24, Prosklad, Muzzone, Ayanmarket, Wipon]
	tasks = []
	for service in services:
		tasks.append(service.send_sms(phone))
	await asyncio.gather(*tasks)
if __name__ == "__main__":
	configure_logs()
	phone = input("Enter phone number: ")
	asyncio.new_event_loop().run_until_complete(main(phone))

