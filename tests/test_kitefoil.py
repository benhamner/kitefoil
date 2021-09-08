import kitefoil
import unittest

class TestKitefoil(unittest.TestCase):
    def test_load_session(self):
        session = kitefoil.KiteFoilSession("gpx/activity_7422746557.gpx")

if __name__ == '__main__':
    unittest.main()
