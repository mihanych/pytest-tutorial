from earth import travel
from earth.travel import Airports


def test_closest_airport():
    assert Airports.YVR == travel.closest_airport("North America")
