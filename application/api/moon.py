from flask import Blueprint, Response
import json
import ephem
from ..moonphase import MoonPhase
import datetime
from datetime import date

moon = Blueprint('moon', __name__)
moon.url_prefix = '/moon'

APPLICATION_JSON = 'application/json'


@moon.route('/')
def index():
    return Response(json.dumps("Moon API"), mimetype=APPLICATION_JSON)


def _validate_inputs(year, month, day):
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        return False

    return True


@moon.route('/phase')
def phase_today():
    m = ephem.Moon()
    today = date.today()
    print(today.strftime('%Y/%m/%d'))
    m.compute(today.strftime('%Y/%m/%d'))
    return Response(json.dumps(MoonPhase(round(m.moon_phase * 100, 1), today.year, today.month, today.day).__dict__),
                    mimetype=APPLICATION_JSON)


@moon.route('/phase/<year>/<month>/<day>')
def phase_specific_day(year, month, day):
    if not _validate_inputs(year, month, day):
        return 'Invalid Request', 400

    m = ephem.Moon()
    m.compute(f'{year}/{month}/{day}')
    return Response(json.dumps(MoonPhase(round(m.moon_phase * 100, 1), year, month, day).__dict__),
                    mimetype=APPLICATION_JSON)

# https://www.moongiant.com/calendar/september/2021
