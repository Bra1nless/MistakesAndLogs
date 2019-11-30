import logging
from my_logging import ger_logger

logger = ger_logger(__name__)
logger1 = ger_logger(__name__, level=logging.DEBUG)


def careful_division(x, y):
    logger1.debug(f"Получены аргументы {x} и {y}")
    if y == 0:
        return 0
    else:
        return x/y


def danger(top, bottom):
    return {
        "result": careful_division(top, bottom),
        "error": None
    }


if __name__ == "__main__":
    for x in range(1,5,2):
        for y in range(-4,2,4):
            if y==0 or x==0:
                logger.info("Кто-то пытается делить на нуль!")
            print(danger(x,y))