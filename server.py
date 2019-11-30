# coding: utf-8
from bottle import route, run, request
from my_logging import ger_logger

logger = ger_logger("divider-server")


@route("/<top:int>/<bottom:int>")
def danger(top, bottom):
    res = {"result": 0, "error": None}
    try:
        res["result"] = top/bottom
    except Exception as err:
        res["error"] = f"Для входных данных {top} и {bottom} не получилось:" \
                       f" {err}"

    agent = request.headers["User-Agent"]
    host = request.headers["Host"]
    path = request.path
    logger.error(f"Ошибки деления при обращении к {host}{path}. "
                 f"User-Agent: {agent}")

    return res


if __name__ == "__main__":
    run(host="localhost", port="8080")
