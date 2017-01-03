from mensaup_api.common.parser import MensaParser
from mensaup_api import options


def get(mensa: str):
    if mensa in options()['mensas']:
        parser = MensaParser(mensa)
        meals = parser.check_page()
        return meals, 200
    return "'{}' is not a known mensa.".format(mensa), 500
