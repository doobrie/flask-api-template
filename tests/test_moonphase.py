from .context import application


def test_moon_phase_formatting():
    mp = application.MoonPhase(1.234, 2021, 9, 23)

    assert mp.phase, '1.2'


def test_moon_phase_date():
    mp = application.MoonPhase(1.234, 2021, 9, 23)

    assert mp.year, 2021
    assert mp.month, 9
    assert mp.day, 23
