from loguru import logger
import sys

def log(func):
    async def make(self, *args, **kwargs): 
        status, text = await func(self, *args, **kwargs)
        service_name = kwargs["url"] if not self.name else self.name
        if status in self.allowed_statuses:
            logger.bind(service = service_name).info(f"OK.")
        else:
            logger.bind(service = service_name, error = text).error(f"{status} HTTP error.")
        await logger.complete()
        return status
    return make

def configure_logs():
    logger.remove(0)
    logger.add(sys.stderr, format = "<green>[{time:YYYY-MM-DD HH:mm:ss:SSS}]</green><blue>[{level}]</blue>[{extra[service]}] - {message}", level = "INFO", colorize = True, filter = lambda record: not record["extra"].get("error", None) and record["extra"].get("service", None), enqueue = True)
    logger.add(sys.stderr, format = "<green>[{time:YYYY-MM-DD HH:mm:ss:SSS}]</green><red>[{level}]</red>[{extra[service]}] - {message}\nError text: {extra[error]}", level = "ERROR", colorize = True, enqueue = True)
    logger.add(sys.stderr, format = "<green>[{time:YYYY-MM-DD HH:mm:ss:SSS}]</green><green>[{level}]</green> - {message}", level = "SUCCESS", filter = lambda record: not record["extra"].get("error", None), colorize = True, enqueue = True)