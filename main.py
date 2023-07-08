import asyncio
from services import Krendel, Enjoy, Zkz, Korzinavdom, Redpark, Nexiopizza, Mechta, Kino, Sxodim, Dinamarket, Ecco, Only, Viled, Dinamarket, Qfilm, Enbek, Aptekaplus, Kaztour, Chinchin, Amanat, Asko, Basel, Boschcenter, Zenge, Technodom, Dns, Koke, Moneyman, Soso, Tengo, Tomi, Lenstore, Hava, Ubet, Winline, Pandora, Kupipolis, Lombardb, Bigroup, Zeta, Tau24, Prosklad, Muzzone, Ayanmarket, Wipon
from services.utils import configure_logs
from loguru import logger
async def main(phone):
	services = [Krendel, Enjoy, Zkz, Korzinavdom, Redpark, Nexiopizza, Mechta, Kino, Sxodim, Dinamarket, Ecco, Only, Viled, Dinamarket, Qfilm, Enbek, Aptekaplus, Kaztour, Chinchin, Amanat, Asko, Basel, Boschcenter, Zenge, Technodom, Dns, Koke, Moneyman, Soso, Tengo, Tomi, Lenstore, Hava, Ubet, Winline, Pandora, Kupipolis, Lombardb, Bigroup, Zeta, Tau24, Prosklad, Muzzone, Ayanmarket, Wipon]

	tasks = []
	for service in services:
		tasks.append(service.send_sms(phone))
	try:
		tasks = await asyncio.gather(*tasks)
	except OSError:
		print("canceling...")
	except RuntimeError:
		print("canceling2...")

if __name__ == "__main__":
	configure_logs()
	try:
		phone = input("Enter phone number: ")
		loop = asyncio.get_event_loop()
		loop.run_until_complete(main(phone))
	except KeyboardInterrupt:
		for task in asyncio.all_tasks(loop=loop):
			task.cancel()
		logger.success("Program finished.")
		

