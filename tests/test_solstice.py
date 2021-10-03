from .context import application


def test_solstice_and_equinox():
    solstice = application.Solstice('a', 'b', 'c', 'd')

    assert solstice.equinox == 'a', 'Solstice is not set correctly'
    assert solstice.autumnal_equinox == 'b', 'Autumnal equinox is not set correctly'
    assert solstice.summer_solstice == 'c', 'Summer solstice is not set correctly'
    assert solstice.winter_solstice == 'd', 'Winter solstice is not set correctly'
