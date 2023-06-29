from loguru import logger
import sys


def enable_logs():
    logger.remove(0)
    logger.add(sys.stderr, format = "<green>[{time:YYYY-MM-DD HH:mm:ss:SSS}]</green><blue>[{level}]</blue>[{extra[service]}] - {message}", level = "INFO", colorize = True, filter = lambda record: not record["extra"].get("error", None), enqueue = True)
    logger.add(sys.stderr, format = "<green>[{time:YYYY-MM-DD HH:mm:ss:SSS}]</green><red>[{level}]</red>[{extra[service]}] - {message}\nError text: {extra[error]}", level = "ERROR", colorize = True, enqueue = True)
