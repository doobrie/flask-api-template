from flask import Blueprint, Response
import json
import ephem
import datetime
from datetime import date
from ..solstice import Solstice

sun = Blueprint('sun', __name__)
sun.url_prefix = '/sun'

APPLICATION_JSON = 'application/json'


@sun.route('/')
def index():
    return Response(json.dumps("Sun API"), mimetype=APPLICATION_JSON)


@sun.route('/equinox')
def phase_today():
    today = date.today()
    year = today.strftime('%Y')

    next_equinox = ephem.next_equinox(year).datetime().strftime('%c')
    next_autumn_equinox = ephem.next_autumn_equinox(
        year).datetime().strftime('%c')
    next_summer_solstice = ephem.next_summer_solstice(
        year).datetime().strftime('%c')
    next_winter_solstice = ephem.next_winter_solstice(
        year).datetime().strftime('%c')

    return Response(json.dumps(Solstice(next_equinox,
                                        next_autumn_equinox,
                                        next_summer_solstice,
                                        next_winter_solstice).__dict__),
                    mimetype=APPLICATION_JSON)
