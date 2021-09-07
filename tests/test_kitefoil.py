import kitefoil
import unittest

class TestKitefoil(unittest.TestCase):
    def test_angle_difference(self):
        self.assertEqual(kitefoil.angle_difference(2,5), 3)
        self.assertEqual(kitefoil.angle_difference(5,2), 3)
        self.assertEqual(kitefoil.angle_difference(2,359), 3)
        self.assertEqual(kitefoil.angle_difference(359,2), 3)
        self.assertEqual(kitefoil.angle_difference(180,0), 180)
        self.assertEqual(kitefoil.angle_difference(0,181), 179)
        self.assertEqual(kitefoil.angle_difference(160,350), 170)

    def test_angle_difference_180(self):
        self.assertEqual(kitefoil.angle_difference_180(2,5), 3)
        self.assertEqual(kitefoil.angle_difference_180(5,2), 3)
        self.assertEqual(kitefoil.angle_difference_180(2,359), 3)
        self.assertEqual(kitefoil.angle_difference_180(359,2), 3)
        self.assertEqual(kitefoil.angle_difference_180(180,0), 0)
        self.assertEqual(kitefoil.angle_difference_180(90,0), 90)
        self.assertEqual(kitefoil.angle_difference_180(0,91), 89)

    def test_load_session(self):
        session = kitefoil.KiteFoilSession("gpx/activity_7422746557.gpx")

if __name__ == '__main__':
    unittest.main()
