# coding: utf-8
from bottle import route, run, request
from my_logging import ger_logger

logger = ger_logger("divider-server")


def tell_me_your_secret():
    logger.info("somebody requests a secret")
    return 42


def careful_division(x, y):
    if y == 0:
        logger.info("Attempt to Zero Division")
        return 0
    else:
        return x/y


@route("/<top:int>/<bottom:int>")
def danger(top, bottom):
    return {
        "result": careful_division(top, bottom),
        "error": None
    }


if __name__ == "__main__":
    run(host="localhost", port="8080")
