import requests
import json
import asyncio
from services import Krendel, Enjoy, Zkz, Korzinavdom, Redpark, Nexiopizza, Mechta, Kino, Sxodim, Dinamarket, Ecco, Only, Viled, Dinamarket, Qfilm, Enbek, Icq, Aptekaplus, Ponyexpress, Kaztour, Chinchin, Amanat, Asko, Basel, Boschcenter, Zenge, Technodom, Dns
from loguru import logger
import sys

async def main(phone):
	services = [Enjoy, Krendel, Zkz, Korzinavdom, Redpark, Nexiopizza, Mechta, Kino, Sxodim, Dinamarket, Ecco, Only, Viled, Qfilm, Enbek, Icq, Aptekaplus, Ponyexpress, Kaztour, Chinchin, Amanat, Asko, Basel, Boschcenter, Zenge, Technodom, Dns]
	tasks = []
	for service in services:
		tasks.append(service.send_sms(phone))
	await asyncio.gather(*tasks)
if __name__ == "__main__":
	logger.remove(0)
	logger.add(sys.stderr, format = "<green>[{time:YYYY-MM-DD HH:mm:ss:SSS}]</green><blue>[{level}]</blue>[{extra[service]}] - {message}", level = "INFO", colorize = True, enqueue = True)
	logger.add(sys.stderr, format = "<green>[{time:YYYY-MM-DD HH:mm:ss:SSS}]</green><red>[{level}]</red>[{extra[service]}] - {message}\nError text: {extra[error]}", level = "ERROR", colorize = True, enqueue = True)
	phone = input("Enter phone number: ")
	asyncio.new_event_loop().run_until_complete(main(phone))

